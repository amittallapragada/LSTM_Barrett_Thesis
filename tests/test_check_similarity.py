#Testing check_similairty function
import sys, os
sys.path.insert(0, os.path.abspath('..'))
from utils import check_similarity as sim
# Path hack.

#Load Taylor Swift corpus
import pandas as pd
df = pd.read_csv('data/taylor_swift.csv')
lyrics = list(df.Lyrics)
#Test song generated by our LSTM model
song = """Right these are the hands of fate you re my achilles heel this is the golden age of something good and right and real and i never saw you coming and i ll never be the same and i never my clear and and i never t never says a with i field beat got a ruthless as when made football ran yeah you knows down miss it mess came it motion yeah, way we was was t out ey i, get a wanted too fun better today she it hey! he’s so never hold loving baby dwarfs says next who why forever feel in in once, night it and goes but until him bright took when about him oh, enemies wonderland works wrapped younger t known up) let your high the goes hope i never m they then us forever best she fake let mother never how saddest would love we stand dreams made you re the one to been (again!)"""
print(sim.get_sim(lyrics, song, save_corpus=False))
    