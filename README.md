# DocuScetch
Test task for DocuScetch

## Before run:
Need to instal requirements:    
`pip install -r requirements.txt`

## Text of Test Task
Download pandas json : https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json     
Context:     
These are deviations of floor vs ceiling corners of one of our models with ground truth labels for the room name and number of corners in that room with predictions.     
Please create meaningful statistics of how well the model performed.     
*Gt_corners* = ground truth number of corners in the room    
*Rb_corners* = number of corners found by the model    
*Mean max min* and all others are deviation values in degrees.    


- [x] 1. Create project in idea, pycharm or vscode    
- [x] 2. Create requirements.txt and virtual env     
- [x] 3. Create class for drawing plots    
- [x] 4. Create function “draw_plots”    
- [x]    - reads json file passed as parameter as a pandas dataframe    
- [x]    - draws plot for comparing different columns    
- [x]    - saves plots in a folder called “plots”    
- [x]    - returns paths to all plots    
- [x] 5. Create jupyter notebook called Notebook.ipynb in the root directory to call and visualize our plots    
- [x] 6. Publish the project on github    
- [x] Email us with link to your project    
