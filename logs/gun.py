loglevel = 'info'
# logfile = '/data/logs/jipin/debug.log' #debug日志
# accesslog = '/data/logs/jipin/access.log'  # gunicorn 访问日志
# errorlog = '/data/logs/jipin/error.log'  # 错误信息日志

accesslog = '-'  # gunicorn 访问日志
errorlog = '-'  # 错误信息日志
# access_log_format = '%(h) -  %(t)s - %(u)s - %(s)s %(H)s'
# 代码更新重启
# loggerclass = 'log_config.CustomLogger'
reload = True
FLASK_ENV = 'sandbox'
