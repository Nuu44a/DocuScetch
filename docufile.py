import matplotlib.pyplot as plt
import pandas as pd
import os


# Creating class for drawing plots
class DoSk():
    '''
        class which contain all logic
    '''
   
    def __init__(self) -> None:
        '''
            initialize variable used for naming plots
        '''
        self.count_pictures = 0
      
        
    def save_picture(self, figure):
        '''
            Takes 'figure' and save it to './plot' directory as 'plot{X}.png'
            {X} generated automaticaly
        '''
        # check for 'plot' directory 
        lnk = os.listdir('.')
        if 'plot' not in lnk:
            os.mkdir('./plot')
        
        # save picture to 'plot' directory
        figure.savefig(f'./plot/plot{self.count_pictures}.png')
        self.count_pictures += 1
    
    
    def plot_comparsion(self, df:pd.DataFrame, *columns):
        '''
            Takes pandas.DataFrame and number of columns and
            drawing plot to compare that columns.
            After that calling .save_picture() to save picture :)
        '''
        fig, ax = plt.subplots()
        fig.set_figheight(6)
        fig.set_figwidth(15)
        
        for column in columns:
            ax.plot(df[column], label=column, alpha=0.5)
                        
        plt.legend()
        plt.title(f'comparsion between {[col for col in columns]}', )
        plt.show()
        
        self.save_picture(fig)
        
    # Creating function “draw_plots”
    def draw_plots(self, json_file):
        '''
            Takes URL or path of JSON file and:
            - read JSON as pandas.DataFrame
            - show info and head of DataFrame
            - draw plot with deviation of prediction from reality
            - call plot_comparsion() to draw pack of plots
            - show count of plots in './plot' directory and print it paths/names
        '''
        # reading json file passed as parameter as a pandas dataframe
        df = pd.read_json(json_file)
        # check whether it was read correctly
        print(df.info())
        print('==============================')
        print(df.head(3))
        
        # draws plot for comparing different columns
        # saves plots in a folder called “plots”
        df['deviation_prediction'] = df['gt_corners'] - df['rb_corners']
        print(df.info())
        fig = df.plot(y='deviation_prediction', figsize=(12,4), title='Deviation of predictions from reality.', grid=True).get_figure()
        self.save_picture(fig)
        
        self.plot_comparsion(df, 'mean', 'max', 'min')
        self.plot_comparsion(df, 'floor_mean', 'floor_max', 'floor_min')
        self.plot_comparsion(df, 'ceiling_mean', 'ceiling_max', 'ceiling_min')
        
        # returns paths to all plots
        lnk = os.listdir('./plot')
        print('count_pictures =', self.count_pictures)
        print('list files in "./plot":', *['./plot/' + name for name in lnk], sep='\n')
                
        return lnk


if __name__ == '__main__':
    print('Message: Just import for Notebook.ipynb')
else:
    print('Message: docufile.py is imported')