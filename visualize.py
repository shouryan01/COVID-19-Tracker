def bokeh_plot(dataF, cat, n_since, tickers, n_top=10):

    ''' Customizations for the Bokeh plots '''
    # cat = {'confirmed', 'deaths', 'recoveries'}
    # n_since = number of cases since we start counting
    # n_top = number of top countries to show
    # tickers = customized tickers for the logy axis. It is simpler to manually define
        # them than to compute them for each case.
    
    from bokeh.io import output_notebook, output_file, show, reset_output
    from bokeh.plotting import figure, save
    from bokeh.models import ColumnDataSource, NumeralTickFormatter, HoverTool
    from bokeh.palettes import Category20

    #Specify the selection tools to be made available
    select_tools = ['box_zoom', 'pan', 'wheel_zoom', 'reset', 'crosshair', 'save']

    # Format the tooltip
    tooltips = [
        ('', '$name'),
        ('Days since', '$x{(0)}'), 
        ('{}'.format(cat), '$y{(0)}')
    ]

    # figure details
    p = figure(y_axis_type="log", plot_width=840, plot_height=600, 
               x_axis_label='Days since average daily {} passed {}'.format(cat, n_since),
               y_axis_label='',
               title=
               'Daily {} ({}-day rolling average) by number of days ' \
               'since {} cases - top {} countries ' \
               '(as of {})'.format(cat, roll, n_since, n_top, yesterday),
               toolbar_location='right',tools=select_tools)

    for i in range(n_top):
        p.line(dataF.index[:], dataF.iloc[:,i], line_width=2, color=Category20[20][i], alpha=0.8, 
               legend_label=dataF.columns[i], name=dataF.columns[i])
        p.circle(dataF.index[:], dataF.iloc[:,i], color=Category20[20][i], fill_color='white',
                 size=3, alpha=0.8, legend_label=dataF.columns[i], name=dataF.columns[i])

    p.yaxis.ticker = tickers

    p.legend.location = 'top_right'
    p.legend.click_policy='hide'

    p.add_tools(HoverTool(tooltips=tooltips))

    output_file('index.html'.format(cat))

    return save(p, 'index.html'.format(cat))
      
yticks = [5,10,20,50,100,200,500,1000,2000]
bokeh_plot(rolling(n_since=3)[1], 'deaths', n_since=3, tickers=yticks)    