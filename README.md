# HKS Insurance Advisory

A responsive insurance and financial services marketplace prototype using React, Vite and a FastAPI demo API.

## Run locally

1. In the project folder, run `npm install` once.
2. Start the website with `npm run dev` and open the local URL printed by Vite (usually `http://localhost:5173`).
3. Optional: start the demo API in a second terminal with `python -m pip install -r backend/requirements.txt` followed by `python -m uvicorn backend.main:app --reload --port 8000`.

The website works without the API. Enquiry form submissions are kept in browser local storage for the prototype and are also sent to the API when it is running. The Admin button shows a local demo lead-assignment dashboard; it is not an authenticated production admin system.

## Included in the prototype

- HKS branded homepage and standalone product detail pages
- Health, life, motor, travel, corporate, finance and investment catalogue sections
- Product search, category filters and shortlist comparison
- Finance, investment and loan information modules
- Loan EMI, investment projection and life cover estimate calculators
- Demo cart summary and mock payment form
- Customer callback form and local enquiry dashboard
- Insights/blog preview and SEO page metadata
- WhatsApp chat link placeholder

## Production integrations still needed

The scope also calls for live WhatsApp Business, CRM, shared lead assignment/follow-up, managed content, Google Analytics/Search Console, deployment SSL and backups. These need account credentials, hosting configuration, a production data store, and security/permission review. The demo checkout does not process payments or store card details. It records no payment transaction and does not issue quotes or bind policies. Product terms and rates are illustrative; finance and investment activity remains subject to applicable permissions.
