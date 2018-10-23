env/bin/python descarga_videos_bellas.py 
env/bin/python descarga_videos_xmf.py 
env/bin/python descarga_videos_carpintero.py
env/bin/python descarga_videos_musikepl.py
cp videos_bellas/docs/static/*json ../visualizations/docs/static 
cd ../visualizations
git commit -a -m updated
git push
