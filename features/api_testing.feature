Feature: Testing API endpoints

  @geolocation_api_testing
  Scenario Outline: Testing Geolocation api if it gives correct response
    When user send <longitude> and <latitude> to API
    Then user gets response with <location> in api response

    Examples:
      | longitude  | latitude   | location |
      | 75.5403866 | 20.9901556 | Jalgaon  |
