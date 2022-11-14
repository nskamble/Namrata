nkdir -p ~/.streamlit/

echo "\
[server]\n\
heatlesss = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
