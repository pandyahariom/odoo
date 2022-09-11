## Compatibility

| Odoo Version |
|---|
| 15.0 |


## Features : RealEstate Module
The Real Estate odoo app supports following functionalities for Property Dealer :

- All available properties are displayed as a list view (tree view) of Real Estate module.
  <img src="https://github.com/pandyahariom/odoo/blob/15.0/custom_addons/realestate/static/HomePage.png">

- Estate Agent can add new property by clicking on the "Create" icon. 
- Agent can fill the details of new property in the form view. [The state of property is set to new].
  <img src="https://github.com/pandyahariom/odoo/blob/15.0/custom_addons/realestate/static/NewProperty.png?">

- At the 2nd Page of notebook of the form view different offers for a particular property can be mentioned.
- Once any offer is received the property state is updated to Offer Received.
- Compute field set the value of best offer automatically based on the maximum value of all offer received.
<img src="https://github.com/pandyahariom/odoo/blob/15.0/custom_addons/realestate/static/offerReceived.png">

- Once any offer is accepted, the "accept" button is disabled from all the offers and the "reject" button available only for the currently accepted offer.
- On acceptance of any offer the state of property is updated to "Offer Accepted".
- If user click on the "reject" button on currently accepted offer, "accept" and "reject" buttons will be re-eanbled for all the offers and property state is reseted to offer received.
<img src="https://github.com/pandyahariom/odoo/blob/15.0/custom_addons/realestate/static/Offers.png?">

- Once user click on the sold button the property state is marked as "Sold". 
- Buttons of "Cancel" and "Sold" will be disabled on sold.
<img src="https://github.com/pandyahariom/odoo/blob/15.0/custom_addons/realestate/static/sold.png?">

- Additional Features : Custom filters, Groups, Search view, constraints, relational fields, auto update of sales person, tags and property type management.

## View Inheritance
- Linking Properties with perticular saleseman in his/her user profile.
[setting -> Users & Company -> Users : In the form view properties are added as a last notebook Page]  
<img src="https://github.com/pandyahariom/odoo/blob/15.0/custom_addons/realestate/static/UserLinking.png?">

## Link module between RealEstate and Account Modules
- Once a property is marked as "sold" the invoice is created for property with line 1) 60% of selling price and 2) 100.0 administrative charge
<img src="https://github.com/pandyahariom/odoo/blob/15.0/custom_addons/realestate/static/InvoicePage.png">


