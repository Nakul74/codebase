# Streamlit basic commands

## streamlit run command

```bash
streamlit run streamlit_app.py --server.port 8080
```
or using nohup
```bash
rm -rf __public_logs__ log_dir && mkdir __public_logs__ && nohup streamlit run streamlit_app.py --server.port 8080 >> __public_logs__/out 2>> __public_logs__/error & echo $! > task_id.txt
```
</br>

## [streamlit auth new library](https://github.com/GauriSP10/streamlit_login_auth_ui)

## [streamlit components](https://streamlit.io/components)