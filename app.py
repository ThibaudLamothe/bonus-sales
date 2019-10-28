import os
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html

# URL definition
img_top_url = 'https://upload.wikimedia.org/wikipedia/commons/7/7e/Invent_Logo_2COL_RGB.png'

# Create application
app = dash.Dash(__name__)
server = app.server

# Page name
app.title = 'Sales - Bonus calculation'

#############################################################################
#                               HTML PAGE
#############################################################################


# Create layout
app.layout = html.Section(
    children=[
        html.Div(
            className='calculPart',
            children=[
                html.Div(html.Img(className='test', src=img_top_url, height="150")),
                html.H1("Application de calcul du Bonus à destination des Sales"),
                html.P("Conformément à la politique établie de l'entreprise, cette page vous permettra de faire la simulation de Bonus."),
                html.Br(),
                html.Div('Entrez votre salaire brut'),
                html.Div(
                    dcc.Input(
                        id='input-box-1',
                        type="number", 
                        placeholder=40000
                    ),
                    # html.P("€"),
                ),
                html.P('Entrez votre coefficient de grade'),
                html.Div(
                    dcc.Input(
                        id='input-box-2',
                        type='number',
                        placeholder=3,
                    ),
                ),
                html.P('Entrez votre nombre de contrat signé'),
                html.Div(
                    dcc.Input(
                        id='input-box-3',
                        type='number',
                        placeholder=5,
                    )
                ),
                html.P(),
                html.Button('Calcul de votre bonus', id='button'),
                html.P(),              
            ]
        ),
        html.P(),
        html.Div(
            className='resultPart',
            children=[
                html.Div(
                    id='output-container-button',
                    children='Remplissez les champs précédents et validez'
                )

            ]
        )
    ]
)

#############################################################################
#                               CALLBACKS
#############################################################################

def create_rep(text, color):
    """
    """
    rep = html.Div(
        children=[text],
        style={'color':color}
    )
    return rep

@app.callback(
    dash.dependencies.Output('output-container-button', 'children'),
    [dash.dependencies.Input('button', 'n_clicks')],
    [dash.dependencies.State('input-box-1', 'value'),
    dash.dependencies.State('input-box-2', 'value'),
    dash.dependencies.State('input-box-3', 'value')]
    )

def bonus_calculation(n_click, salaire, coef, contrat):
    # Première fois, renvoie une valeur par défaut
    if n_click is None:
        text = "Calcul du bonus à venir. Merci de remplir les champs."
        return create_rep(text, 'black')

    try:
        # Conversion des valeurs indiquées
        salaire = int(salaire)
        contrat = int(contrat)
        coef = int(coef)

        # Calcul du bonus
        bonus = (salaire + contrat * 5000)* (1 + 0.1 * coef) / 10
        bonus = np.round(bonus, 2)
    
    except:
        text = "Remplissez les 3 champs pour connaitre votre bonus."
        return create_rep(text, 'red')
    
    # Si tout est en règle on renvoie le bonus
    text = 'Votre bonus annuel sera de  {} €.'.format(str(bonus))
    return create_rep(text, 'green')


#############################################################################
#                               RUNNING APPLICATION
#############################################################################


if __name__ == '__main__':
    app.run_server(debug=True)