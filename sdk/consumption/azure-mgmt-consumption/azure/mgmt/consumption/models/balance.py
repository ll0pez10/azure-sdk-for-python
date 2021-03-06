# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource import Resource


class Balance(Resource):
    """A balance resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar currency: The ISO currency in which the meter is charged, for
     example, USD.
    :vartype currency: str
    :ivar beginning_balance: The beginning balance for the billing period.
    :vartype beginning_balance: decimal.Decimal
    :ivar ending_balance: The ending balance for the billing period (for open
     periods this will be updated daily).
    :vartype ending_balance: decimal.Decimal
    :ivar new_purchases: Total new purchase amount.
    :vartype new_purchases: decimal.Decimal
    :ivar adjustments: Total adjustment amount.
    :vartype adjustments: decimal.Decimal
    :ivar utilized: Total Commitment usage.
    :vartype utilized: decimal.Decimal
    :ivar service_overage: Overage for Azure services.
    :vartype service_overage: decimal.Decimal
    :ivar charges_billed_separately: Charges Billed separately.
    :vartype charges_billed_separately: decimal.Decimal
    :ivar total_overage: serviceOverage + chargesBilledSeparately.
    :vartype total_overage: decimal.Decimal
    :ivar total_usage: Azure service commitment + total Overage.
    :vartype total_usage: decimal.Decimal
    :ivar azure_marketplace_service_charges: Total charges for Azure
     Marketplace.
    :vartype azure_marketplace_service_charges: decimal.Decimal
    :param billing_frequency: The billing frequency. Possible values include:
     'Month', 'Quarter', 'Year'
    :type billing_frequency: str or
     ~azure.mgmt.consumption.models.BillingFrequency
    :ivar price_hidden: Price is hidden or not.
    :vartype price_hidden: bool
    :ivar new_purchases_details: List of new purchases.
    :vartype new_purchases_details:
     list[~azure.mgmt.consumption.models.BalancePropertiesNewPurchasesDetailsItem]
    :ivar adjustment_details: List of Adjustments (Promo credit, SIE credit
     etc.).
    :vartype adjustment_details:
     list[~azure.mgmt.consumption.models.BalancePropertiesAdjustmentDetailsItem]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'tags': {'readonly': True},
        'currency': {'readonly': True},
        'beginning_balance': {'readonly': True},
        'ending_balance': {'readonly': True},
        'new_purchases': {'readonly': True},
        'adjustments': {'readonly': True},
        'utilized': {'readonly': True},
        'service_overage': {'readonly': True},
        'charges_billed_separately': {'readonly': True},
        'total_overage': {'readonly': True},
        'total_usage': {'readonly': True},
        'azure_marketplace_service_charges': {'readonly': True},
        'price_hidden': {'readonly': True},
        'new_purchases_details': {'readonly': True},
        'adjustment_details': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'currency': {'key': 'properties.currency', 'type': 'str'},
        'beginning_balance': {'key': 'properties.beginningBalance', 'type': 'decimal'},
        'ending_balance': {'key': 'properties.endingBalance', 'type': 'decimal'},
        'new_purchases': {'key': 'properties.newPurchases', 'type': 'decimal'},
        'adjustments': {'key': 'properties.adjustments', 'type': 'decimal'},
        'utilized': {'key': 'properties.utilized', 'type': 'decimal'},
        'service_overage': {'key': 'properties.serviceOverage', 'type': 'decimal'},
        'charges_billed_separately': {'key': 'properties.chargesBilledSeparately', 'type': 'decimal'},
        'total_overage': {'key': 'properties.totalOverage', 'type': 'decimal'},
        'total_usage': {'key': 'properties.totalUsage', 'type': 'decimal'},
        'azure_marketplace_service_charges': {'key': 'properties.azureMarketplaceServiceCharges', 'type': 'decimal'},
        'billing_frequency': {'key': 'properties.billingFrequency', 'type': 'str'},
        'price_hidden': {'key': 'properties.priceHidden', 'type': 'bool'},
        'new_purchases_details': {'key': 'properties.newPurchasesDetails', 'type': '[BalancePropertiesNewPurchasesDetailsItem]'},
        'adjustment_details': {'key': 'properties.adjustmentDetails', 'type': '[BalancePropertiesAdjustmentDetailsItem]'},
    }

    def __init__(self, **kwargs):
        super(Balance, self).__init__(**kwargs)
        self.currency = None
        self.beginning_balance = None
        self.ending_balance = None
        self.new_purchases = None
        self.adjustments = None
        self.utilized = None
        self.service_overage = None
        self.charges_billed_separately = None
        self.total_overage = None
        self.total_usage = None
        self.azure_marketplace_service_charges = None
        self.billing_frequency = kwargs.get('billing_frequency', None)
        self.price_hidden = None
        self.new_purchases_details = None
        self.adjustment_details = None
