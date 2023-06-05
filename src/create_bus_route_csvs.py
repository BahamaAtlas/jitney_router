import csv

def create_bus_route_csvs(route):
    #create index of routes
    route_number_match = ['1', '1A', '2', '2A', '3', '3A', '4', '4A', '5', '5A', '6', '6A', '7', '7A', '8', '8A', '9', '9A', '9B', '10', '10A', '10B', '11', '11A', '12', '14', '14A', '15', '15A', '16', '16A', '16B', '17', '17A', '18', '19', '20', '21', '21A', '22', '22A', '23']   
    # Extract the service area
    service_area = route.split('\n')[0].strip()
    # Extract the route number and starting point
    route_number = route[0]
    starting_point = route.split('\n')[0]
    # Extract the street names
    street_names = route.split('\n')[1].split('/')
    
    # Create a new CSV file for the route
    number = routes.index(route)
    csv_filename = f'Route_{route_number_match[number]}.csv'
    
    df = pd.DataFrame(columns = ['Service Area', 'Route Number', 'Starting Point', 'Street Names'])
    df['Street Names'] = street_names
    df['Service Area'] = service_area
    df['Route Number'] = route_number
    df['Starting Point'] = starting_point
    
    df.to_csv(f'{csv_filename}')
    print(route)

for i in range(0,42):
    route = routes[i]
    router_csv(route)
