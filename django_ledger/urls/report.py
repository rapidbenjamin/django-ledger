from django.urls import path

from django_ledger import views

urlpatterns = [

    # BALANCE SHEET Reports...
    # Entities...
    path('entity/<slug:entity_slug>/balance-sheet/',
         views.EntityModelBalanceSheetView.as_view(),
         name='entity-bs'),
    path('entity/<slug:entity_slug>/balance-sheet/year/<int:year>/',
         views.FiscalYearEntityModelBalanceSheetView.as_view(),
         name='entity-bs-year'),
    path('entity/<slug:entity_slug>/balance-sheet/quarter/<int:year>/<str:quarter>/',
         views.QuarterlyEntityModelBalanceSheetView.as_view(),
         name='entity-bs-quarter'),
    path('entity/<slug:entity_slug>/balance-sheet/month/<int:year>/<str:month>/',
         views.MonthlyEntityModelBalanceSheetView.as_view(),
         name='entity-bs-month'),
    path('entity/<slug:entity_slug>/balance-sheet/date/<int:year>/<int:month>/<int:day>/',
         views.DateEntityModelBalanceSheetView.as_view(),
         name='entity-bs-date'),

    # Ledgers....
    path('ledger/<slug:entity_slug>/<uuid:ledger_pk>/balance-sheet/year/<int:year>/',
         views.FiscalYearLedgerBalanceSheetView.as_view(),
         name='ledger-bs-year'),
    path('ledger/<slug:entity_slug>/<uuid:ledger_pk>/balance-sheet/quarter/<int:year>/<int:quarter>/',
         views.QuarterlyLedgerBalanceSheetView.as_view(),
         name='ledger-bs-quarter'),
    path('ledger/<slug:entity_slug>/<uuid:ledger_pk>/balance-sheet/month/<int:year>/<str:month>/',
         views.MonthlyLedgerBalanceSheetView.as_view(),
         name='ledger-bs-month'),

    # Units...
    path('unit/<slug:entity_slug>/<slug:unit_slug>/balance-sheet/',
         views.EntityUnitModelBalanceSheetView.as_view(),
         name='unit-bs'),
    path('unit/<slug:entity_slug>/<slug:unit_slug>/balance-sheet/year/<int:year>/',
         views.FiscalYearEntityUnitModelBalanceSheetView.as_view(),
         name='unit-bs-year'),
    path('unit/<slug:entity_slug>/<slug:unit_slug>/balance-sheet/quarter/<int:year>/<int:quarter>/',
         views.QuarterlyEntityUnitModelBalanceSheetView.as_view(),
         name='unit-bs-quarter'),
    path('unit/<slug:entity_slug>/<slug:unit_slug>/balance-sheet/month/<int:year>/<str:month>/',
         views.MonthlyEntityUnitModelBalanceSheetView.as_view(),
         name='unit-bs-month'),

    # INCOME STATEMENT Reports ----
    # Entity .....
    path('entity/<slug:entity_slug>/income-statement/',
         views.EntityModelIncomeStatementView.as_view(),
         name='entity-ic'),
    path('entity/<slug:entity_slug>/income-statement/year/<int:year>/',
         views.FiscalYearEntityModelIncomeStatementView.as_view(),
         name='entity-ic-year'),
    path('entity/<slug:entity_slug>/income-statement/quarter/<int:year>/<str:quarter>/',
         views.QuarterlyEntityModelIncomeStatementView.as_view(),
         name='entity-ic-quarter'),
    path('entity/<slug:entity_slug>/income-statement/month/<int:year>/<str:month>/',
         views.MonthlyEntityModelIncomeStatementView.as_view(),
         name='entity-ic-month'),

    # Ledgers ....
    path('ledger/<slug:entity_slug>/<uuid:ledger_pk>/income-statement/year/<int:year>/',
         views.FiscalYearLedgerIncomeStatementView.as_view(),
         name='ledger-ic-year'),
    path('ledger/<slug:entity_slug>/<uuid:ledger_pk>/income-statement/quarter/<int:year>/<int:quarter>/',
         views.QuarterlyLedgerIncomeStatementView.as_view(),
         name='ledger-ic-quarter'),
    path('ledger/<slug:entity_slug>/<uuid:ledger_pk>/income-statement/month/<int:year>/<str:month>/',
         views.MonthlyLedgerIncomeStatementView.as_view(),
         name='ledger-ic-month'),

    # Entity Units...
    path('unit/<slug:entity_slug>/<slug:unit_slug>/income-statement/',
         views.EntityUnitModelIncomeStatementView.as_view(),
         name='unit-ic'),
    path('unit/<slug:entity_slug>/<slug:unit_slug>/income-statement/year/<int:year>/',
         views.FiscalYearEntityUnitModelIncomeStatementView.as_view(),
         name='unit-ic-year'),
    path('unit/<slug:entity_slug>/<slug:unit_slug>/income-statement/quarter/<int:year>/<int:quarter>/',
         views.QuarterlyEntityUnitModelIncomeStatementView.as_view(),
         name='unit-ic-quarter'),
    path('unit/<slug:entity_slug>/<slug:unit_slug>/income-statement/month/<int:year>/<str:month>/',
         views.MonthlyEntityUnitModelIncomeStatementView.as_view(),
         name='unit-ic-month'),

]
