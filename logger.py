import logging

log = logging.getLogger(__name__)

logging.basicConfig(**settings.LOGGERS[settings.dicionariodeconfi['color']])

dicionariodeconfi = {
'color': {
		'datefmt'  : '%Y-%m-%d %H:%M:%S',
		'format'   : f'[{Fore.CYAN}%(asctime)s.%(msecs)03d{Style.RESET_ALL}]'
				     f'[{Fore.MAGENTA}%(process)s{Style.RESET_ALL}]'
				     f'[{Fore.RED}%(threadName)s{Style.RESET_ALL}]'
				     f'[{Fore.GREEN}%(module)s:%(funcName)s:%(lineno)d{Style.RESET_ALL}]'
				     f'[{Fore.YELLOW}%(levelname)s{Style.RESET_ALL}]'
				     f'{Style.RESET_ALL}'
				     f': %(message)s',
		'level'    : logging.DEBUG,
		'stream'   : sys.stdout
	}
  }
