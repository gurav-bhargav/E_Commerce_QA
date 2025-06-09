Feature: Testing home page features

  @sortingTesting
  Scenario Outline: Testing sorting feature
    Given user login and is on home page
    When user sort products by <option>
    Then user validate the order

    Examples:
      | option              |
      | Name (Z to A)       |
      | Price (low to high) |
      | Price (high to low) |

  @E2E_AddToCart
  Scenario Outline: Checking End To End flow of order placing
    Given user login and is on home page
    When user add product named <name_of_product> to cart and navigate to cart
    And user validate product in cart and continue
    And user provide details and checkout
    Then user should get order confirmation

    Examples:
      | name_of_product         |
      | Sauce Labs Bolt T-Shirt |
      | Sauce Labs Onesie       |
