import psycopg2
import psycopg2.extras

DATABASE_CONNECTION = {
	'host'    : '',
	'port'    : '',
	'dbname'  : '',
	'user'    : '',
	'password': ''
}

    log.debug(f"Conectando ao banco de dados: {settings.DATABASE_CONNECTION}")
		try:
			self.conn = psycopg2.connect(**settings.DATABASE_CONNECTION)
			self.conn.autocommit = True
      with self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
			try:
				sql = cur.mogrify("""
						UPDATE
							public.tabela
						SET
							ultima_execucao = now()
						WHERE
							id_loja = %s;
						""",(id_loja,))
				log.debug(sql)
				cur.execute(sql)
        retorno = cur.fetchall()
		except psycopg2.Error as e:
			raise ProcessorException(f'Erro de conexao ao banco e dados: {e}')
