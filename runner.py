from behave.__main__ import main

if __name__ == '__main__':
    main([
        '--tags=@E2E_AddToCart,@geolocation_api_testing,@sortingTesting,@testLogin',
        '--format=allure_behave.formatter:AllureFormatter',
        '--outfile=reports/allure-results',
        'features/'
    ])