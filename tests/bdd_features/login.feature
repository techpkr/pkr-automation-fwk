Feature: User

  @bdd
  Scenario: Successful login with valid credentials
    Given the API endpoint is "core/api/v1/login"
    When I make a "POST" request to the API with auth header
    Then the status code should be 200
    And the response contains the nonempty attribute "token"
