import asyncio, logging, aiomysql


# #建立输出函数
def log(sql, args=()):
    logging.info('SQL:%s' % sql)


# #异步IO函数
async def create_pool(loop, **kw):
    logging.info('create database connection pool...')
    global __pool
    __pool = await aiomysql.create_pool(
        host=kw.get('host', 'locahost'),
        port=kw.get('port', 3306),
        user=kw['user'],
        psaaword=kw['password'],
        db=['db'],
        charset=kw.get['charset', 'utf8'],
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize',10),
        minsize=kw.get('minsize',1),
        loop=loop
        )


# 添加select语句
async def select(sql, args, size=None):
    log(sql, args)
    global __pool
    with (await __pool) as conn:
        cur = await conn.cursor(aiomysql.DictCursor)
        await cur.execute(sql.replace('?', '%s'), args or ())
        






































