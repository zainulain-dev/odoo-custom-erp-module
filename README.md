# Custom ERP & CRM Module (Odoo 18)

A custom Odoo 18 module designed to extend core CRM and Sales functionalities. This module adds advanced tracking, automated workflows, and custom PDF reporting.

## 🛠 Tech Stack
- **Backend:** Python, Odoo ORM
- **Frontend:** XML Views, JavaScript (OWL)
- **Database:** PostgreSQL
- **Reporting:** QWeb Templates

## ✨ Key Features
- **Model Inheritance:** Extended `res.partner` to include `x_crm_tracking_id` and `x_is_vip_client`. Extended `sale.order` with `x_custom_notes` and computed `x_total_weight`.
- **Custom Views:** Designed Form and List view inheritances using XPath to seamlessly integrate new fields.
- **Automated Actions:** Configured a Server Action ("Send Custom VIP Email") bound to `sale.order` utilizing `message_post` for chatter logging.
- **Security:** Implemented role-based access control using `ir.model.access.csv` for Sales and Admin groups.
- **Reporting:** Generated a custom QWeb PDF report inheriting `sale.report_saleorder_document` with a custom A4 paper format.

## 📁 Module Structure
```
custom_erp_crm/
├── models/    # Python model inheritance and computed fields
├── views/     # XML UI extensions (Form & Tree views)
├── security/  # Access rights (ir.model.access.csv)
├── reports/   # QWeb templates and paper formats
└── data/      # Server actions and automation rules
```
