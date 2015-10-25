CONFIG = {
        'mode': 'wsgi',
        'working_dir': '/home/carry/Web/Web1/ask_Lavrinenko',
        'user': 'www-data',
        'group': 'www-data',
        'args': (
		'--bind=127.0.0.1:8081',
		'--timeout=30',
                'wsgi:application',
        ),
}

