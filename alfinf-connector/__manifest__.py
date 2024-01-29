# Copyright 2024 Manuel Calero - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Alfinf Connector",
    "summary": "Alfinf Connector",
    "version": "16.0.1.0.0",
    "development_status": "Beta",
    "license": "AGPL-3",
    "author": "Alfinf",
    "website": "https://github.com/alfinfsi/",
    "category": "Connector",
    "depends": [
        "sale",
        "sale_management",
        "contacts",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/sale_order_view.xml",
        "views/sale_order_line_view.xml",
        "views/res_partner_view.xml",
        "views/product_template_view.xml",
        "views/alfinf_trace_view.xml",
        "views/alfinf_family_view.xml",
        "views/alfinf_variedad_view.xml",
    ],
    "installable": True,
}
