Feature: Test With A Lot Of Data
    --------------------------------------------------------------------------------------------------------
    haha, sql goes brr
    --------------------------------------------------------------------------------------------------------
    
  Scenario Outline: Test Autogenerated Payload
    Given The numbers <number> and <multiplier>
    Then The answer is it doubled
      Examples:
        | number | multiplier |
        | 1      | 2          |
        | 2      | 2          |
        | 3      | 2          |
        | 4      | 2          |
        | 5      | 2          |
        | 6      | 2          |
        | 7      | 2          |