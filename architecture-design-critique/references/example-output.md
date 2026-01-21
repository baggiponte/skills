# Example Output

A completed critique for a hypothetical e-commerce codebase.

## Architectural Inventory (Phase 1 Summary)

**Project Overview**
- Language/Framework: Node.js 18 + Express + TypeScript
- Build System: npm scripts, tsc
- Key Dependencies: Sequelize, ioredis, stripe-node, nodemailer

**Entry Points**
| Type | Location | Count |
|------|----------|-------|
| HTTP Routes | `routes/*.ts` | 24 endpoints |
| Background Workers | `workers/*.ts` | 3 job processors |
| Cron Jobs | `cron/daily.ts` | 2 scheduled tasks |

**Services**
| Service | Location | Dependencies |
|---------|----------|--------------|
| UserService | `services/user.ts` | UserRepo, EmailService |
| OrderService | `services/order.ts` | OrderRepo, PaymentService, InventoryService |
| PaymentService | `services/payment.ts` | Stripe client |

**Infrastructure**
| Component | Type | Access Pattern |
|-----------|------|----------------|
| PostgreSQL | Database | Sequelize ORM, direct connection |
| Redis | Cache | ioredis client, no abstraction |
| Stripe | Payment API | Direct SDK calls in PaymentService |
| SendGrid | Email | nodemailer transport in EmailService |

**Domain Model**
| Entity | Location | Relationships |
|--------|----------|---------------|
| User | `models/user.ts` | hasMany Orders |
| Order | `models/order.ts` | belongsTo User, hasMany LineItems |
| Product | `models/product.ts` | hasMany LineItems |
| Cart | `models/cart.ts` | belongsTo User, hasMany CartItems |

**Observed Patterns**: Active Record via Sequelize, service classes for orchestration, no repository layer, direct infrastructure access from services.

## Assessment (Phase 2 Summary)

**Executive Summary**

This e-commerce codebase has a solid foundation with clear service boundaries and proper separation of background jobs from request handling. The team has established reasonable conventions that have served them well.

However, the architecture shows signs of organic growth without consistent application of dependency inversion principles. Domain logic has leaked into infrastructure concerns—pricing calculations live inside ORM hooks, and payment processing is tightly coupled to Stripe's SDK. These issues don't cause immediate pain, but they're accumulating technical debt that will slow feature development and make testing increasingly difficult.

The thesis: *This codebase handles feature organization well, but struggles with clean separation between domain logic and infrastructure dependencies.*

**What's Working Well**
- Clear feature folder organization
- Service layer exists for complex operations
- Background jobs properly separated from HTTP handlers

**Detailed Findings**

### Finding 1: Pricing Logic Embedded in ORM Hooks

**Category**: Boundary Violation

**The Problem**
The `Order` model contains pricing calculation logic inside Sequelize lifecycle hooks. When an order is saved, the `beforeSave` hook recalculates totals, applies discounts, and computes tax. This mixes pure business rules with persistence mechanics.

**Why It Matters**
- Cannot unit test pricing without a database connection
- Pricing rules are invisible—hidden inside ORM hooks rather than explicit domain code
- Changing pricing logic requires understanding Sequelize hook execution order

**Evidence**
- `models/order.ts:45-78` - `beforeSave` hook with 30+ lines of pricing logic
- `models/order.ts:82` - Tax calculation references `process.env.TAX_RATE` directly

**Suggested Direction**
Extract a pure `PricingCalculator` class that takes order data and returns computed totals. Hook simply calls calculator and assigns results.

---

### Finding 2: Direct Payment Provider Coupling

**Category**: Boundary Violation

**The Problem**
`CartService` directly instantiates and calls Stripe SDK methods. Payment intent creation, charge capture, and refund logic all reference Stripe-specific types and error codes.

**Why It Matters**
- Switching payment providers requires rewriting business logic
- Cannot test checkout flow without Stripe test mode
- Stripe version upgrades have unbounded blast radius

**Evidence**
- `services/cart.ts:112-145` - Direct `stripe.paymentIntents.create()` calls
- `services/cart.ts:167` - Catches `Stripe.errors.CardError` specifically

**Suggested Direction**
Introduce `PaymentGateway` port interface. Current Stripe logic becomes `StripePaymentAdapter`.

## Roadmap (Phase 3 Summary)

**Executive Summary**

This roadmap contains 2 quick wins, 2 medium-term improvements, and 2 long-term projects. Start with the `PricingCalculator` extraction—it's the lowest-risk change with immediate testability benefits, and it establishes a pattern the team can follow for subsequent extractions.

The quick wins are independent and can be tackled in any order. Medium-term items should follow quick wins, as they build on the patterns established. Long-term items require the foundation laid by earlier work.

**Quick Wins**

### 1. Extract PricingCalculator from Order Model

**Problem**: Pricing logic buried in ORM hooks makes testing require database setup.
**Impact**: Enables unit testing of pricing rules; makes pricing logic explicit and auditable.

**Implementation Approach**

1. Create the pricing domain module:
   ```typescript
   // domain/pricing/calculator.ts
   interface OrderLineItem {
     unitPrice: number;
     quantity: number;
     discountPercent?: number;
   }

   interface PricingResult {
     subtotal: number;
     discount: number;
     tax: number;
     total: number;
   }

   export function calculateOrderTotal(
     items: OrderLineItem[],
     taxRate: number
   ): PricingResult {
     const subtotal = items.reduce((sum, item) =>
       sum + (item.unitPrice * item.quantity), 0);
     // ... rest of logic extracted from hook
   }
   ```

2. Update the Order model hook:
   ```typescript
   // models/order.ts
   import { calculateOrderTotal } from '../domain/pricing/calculator';

   Order.beforeSave((order) => {
     const result = calculateOrderTotal(order.lineItems, config.taxRate);
     Object.assign(order, result);
   });
   ```

**Files to Modify**
- `domain/pricing/calculator.ts` (new)
- `models/order.ts:45-78` (simplify hook)

**Verification**
- Add unit tests for `calculateOrderTotal` with various scenarios
- Existing integration tests should pass unchanged

---

### 2. Create PaymentGateway Interface

**Problem**: Direct Stripe coupling prevents testing and locks in vendor.
**Impact**: Enables mock payment testing; prepares for potential provider switch.

**Implementation Approach**

1. Define the port:
   ```typescript
   // domain/ports/payment-gateway.ts
   export interface PaymentGateway {
     createPaymentIntent(amount: number, currency: string): Promise<PaymentIntent>;
     capturePayment(intentId: string): Promise<PaymentResult>;
     refund(chargeId: string, amount?: number): Promise<RefundResult>;
   }
   ```

2. Implement Stripe adapter:
   ```typescript
   // infrastructure/stripe-payment-adapter.ts
   export class StripePaymentAdapter implements PaymentGateway {
     constructor(private stripe: Stripe) {}

     async createPaymentIntent(amount: number, currency: string) {
       const intent = await this.stripe.paymentIntents.create({ amount, currency });
       return { id: intent.id, clientSecret: intent.client_secret };
     }
     // ... other methods
   }
   ```

3. Inject into CartService constructor and update calls.

**Files to Modify**
- `domain/ports/payment-gateway.ts` (new)
- `infrastructure/stripe-payment-adapter.ts` (new)
- `services/cart.ts:112-167` (use injected gateway)

**Medium-term**

3. Introduce repository pattern for data access
4. Implement dependency injection container

**Long-term**

5. Separate read models for reporting queries
6. Extract order fulfillment bounded context
