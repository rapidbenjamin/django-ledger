# todo: will develop a roles manager

# --- ASSET ROLES ----
# ROLE_PARENT_ASSET = 'parent_asset'

# Current Assets ---
ROLE_CA_CASH = 'asset_ca_cash'
ROLE_CA_MKT_SECURITIES = 'asset_ca_mkt_sec'
ROLE_CA_RECEIVABLES = 'asset_ca_recv'
ROLE_CA_INVENTORY = 'asset_ca_inv'
ROLE_CA_UNCOLLECTIBLES = 'asset_ca_uncoll'
ROLE_CA_PREPAID = 'asset_ca_prepaid'
ROLE_CA_OTHER = 'asset_ca_other'

# Long Term Investments ---
ROLE_LTI_NOTES_RECEIVABLE = 'asset_lti_notes'
ROLE_LTI_LAND = 'asset_lti_land'
ROLE_LTI_SECURITIES = 'asset_lti_sec'

# Property, Plat & Equipment ---
ROLE_PPE = 'asset_ppe'

# Intangible Assets ---
ROLE_INTANGIBLE_ASSETS = 'asset_ia'

# Other Asset Adjustments ---
ROLE_ASSET_OTHER = 'asset_other'

# LIABILITIES ----

# Current Liabilities
ROLE_CL_ACC_PAYABLE = 'lia_cl_acc_pay'
ROLE_CL_WAGES_PAYABLE = 'lia_cl_wage_pay'
ROLE_CL_INT_PAYABLE = 'lia_cl_wage_pay'
ROLE_CL_ST_NOTES_PAYABLE = 'lia_cl_st_notes_payable'
ROLE_CL_LTD_MATURITIES = 'lia_cl_ltd_mat'
ROLE_CL_DEFERRED_REVENUE = 'lia_cl_def_rev'
ROLE_CL_OTHER = 'lia_cl_other'

# Long Term Liabilities ---
# ROLE_LTL = 'lia_ltl'
# ROLE_LTL = 'lia_ltl'
ROLE_LTL_NOTES_PAYABLE = 'lia_ltl_notes'
ROLE_LTL_BONDS_PAYABLE = 'lia_ltl_bonds'
ROLE_LTL_MORTAGE_PAYABLE = 'lia_ltl_mortgage'

# ROLE_EQ_CAPITAL_ADJ = 'cap_adj'
ROLE_EQ_CAPITAL = 'eq_capital'
ROLE_EQ_ADJ = 'eq_adj'
ROLE_EQ_COMMON_STOCK = 'eq_stock_c'
ROLE_EQ_PREFERRED_STOCK = 'eq_stock_p'

ROLE_INCOME_SALES = 'in_sales'
ROLE_INCOME_PASSIVE = 'in_pass'
ROLE_INCOME_OTHER = 'in_other'

# COGS ---
ROLE_COGS = 'ex_cogs'

# ROLE_EXPENSES = 'ex'
ROLE_EXPENSES_OP = 'ex_op'
ROLE_EXPENSES_CAPITAL = 'ex_cap'
ROLE_EXPENSES_TAXES = 'ex_taxes'
ROLE_EXPENSES_INTEREST = 'ex_interest'
ROLE_EXPENSES_OTHER = 'ex_other'

ROLES_QUICK_ASSETS = [
    ROLE_CA_CASH,
    ROLE_CA_MKT_SECURITIES
]

ROLES_CURRENT_ASSETS = [
    ROLE_CA_CASH,
    ROLE_CA_MKT_SECURITIES,
    ROLE_CA_INVENTORY,
    ROLE_CA_RECEIVABLES,
    ROLE_CA_PREPAID,
    ROLE_CA_OTHER
]

ROLES_ASSETS = ROLES_CURRENT_ASSETS + [
    ROLE_LTI_NOTES_RECEIVABLE,
    ROLE_LTI_LAND,
    ROLE_LTI_SECURITIES,
    ROLE_PPE,
    ROLE_INTANGIBLE_ASSETS,
    ROLE_ASSET_OTHER
]

ROLES_CURRENT_LIABILITIES = [
    ROLE_CL_ACC_PAYABLE,
    ROLE_CL_DEFERRED_REVENUE,
    ROLE_CL_INT_PAYABLE,
    ROLE_CL_LTD_MATURITIES,
    ROLE_CL_OTHER,
    ROLE_CL_ST_NOTES_PAYABLE,
    ROLE_CL_WAGES_PAYABLE
]

ROLES_LIABILITIES = ROLES_CURRENT_LIABILITIES + [
    ROLE_LTL_NOTES_PAYABLE,
    ROLE_LTL_BONDS_PAYABLE,
    ROLE_LTL_MORTAGE_PAYABLE,
]

ROLES_CAPITAL = [
    ROLE_EQ_CAPITAL,
    ROLE_EQ_COMMON_STOCK,
    ROLE_EQ_PREFERRED_STOCK,
    ROLE_EQ_ADJ
]

ROLES_INCOME = [
    ROLE_INCOME_SALES,
    ROLE_INCOME_PASSIVE,
    ROLE_INCOME_OTHER,
]

ROLES_EXPENSES = [
    ROLE_COGS,
    ROLE_EXPENSES_OP,
    ROLE_EXPENSES_INTEREST,
    ROLE_EXPENSES_TAXES,
    ROLE_EXPENSES_CAPITAL,
    ROLE_EXPENSES_OTHER
]

ROLES_NET_PROFIT = [
    ROLE_INCOME_SALES,
    ROLE_INCOME_PASSIVE,
    ROLE_INCOME_OTHER,
    ROLE_COGS,
]

ROLES_GROSS_PROFIT = [
    ROLE_INCOME_SALES,
    ROLE_COGS
]

ROLES_NET_SALES = [
    ROLE_INCOME_SALES,
    ROLE_INCOME_PASSIVE
]

ROLES_EARNINGS = ROLES_INCOME + ROLES_EXPENSES
