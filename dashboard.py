import dash
from dash import dcc, html

# Initialize Dash app
app = dash.Dash(__name__)

# Define layout with gradient background and centered content
app.layout = html.Div(
    style={
        'background': 'linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url("/assets/background.png")',
        'background-size': 'cover',
        'background-position': 'center',
        'height': '230vh',  # Adjust height to cover entire viewport
        'display': 'flex',
        'flex-direction': 'column',
        'justify-content': 'center',
        'align-items': 'center',
        'text-align': 'center',
        'color': 'white',  # Set text color to contrast with dark background
        'font-family': 'Arial, sans-serif',  # Example font family
    },
    children=[
        html.H1("Lending Club Loan Data", style={'margin-bottom': '20px'}),
        html.H2("Loan Data Dashboard", style={'margin-bottom': '20px'}),
        html.Div([
                html.H2("Purpose of Loan", style={'margin-bottom': '10px'}),
            html.Img(src='/assets/purpose_count.png', style={'width': '50%'}),
            html.P("The most common purpose for loans in the dataset is debt consolidation, "
                    "accounting for approximately 51.8% of all loans.\n"
                    "Credit card loans follow with about 23.9%.\n" 
                    "Educational loans are the least frequent, making up only 0.1% of the total loans.",
                    style={'margin-left': '20px'}),
    
        ]),
        html.Div([
            html.H2("Loan Amount Distribution", style={'margin-bottom': '10px'}),
            html.Img(src='/assets/loan_amnt.png', style={'width': '52%'}),
        ]),
        html.Div([
            html.H2("Bad Loans Analysis", style={'margin-bottom': '10px'}),
            html.Img(src='/assets/badloan.png', style={'width': '50%'}),
        ]),
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
