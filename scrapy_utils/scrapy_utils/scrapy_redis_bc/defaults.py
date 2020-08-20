import redis
import rediscluster

# For standalone use.
DUPEFILTER_KEY = 'dupefilter:%(timestamp)s'

PIPELINE_KEY = '%(spider)s:items'

REDIS_CLS = redis.StrictRedis
REDIS_ENCODING = 'utf-8'
# Sane connection defaults.
REDIS_PARAMS = {
    'socket_timeout': 30,
    'socket_connect_timeout': 30,
    'retry_on_timeout': True,
    'encoding': REDIS_ENCODING,
}

SCHEDULER_QUEUE_KEY = '%(spider)s:requests'
SCHEDULER_QUEUE_CLASS = 'scrapy_utils.scrapy_redis_bc.queue.PriorityQueue'
SCHEDULER_DUPEFILTER_KEY = '%(spider)s:dupefilter'
SCHEDULER_DUPEFILTER_CLASS = 'scrapy_utils.scrapy_redis_bc.dupefilter.RFPDupeFilter'
SCHEDULER_PERSIST = True

START_URLS_KEY = '%(name)s:start_urls'
START_URLS_AS_SET = False

# Defaults Bloom Filter Settings
BLOOMFILTER_HASH_NUMBER = 6
BLOOMFILTER_BIT = 22

REDIS_CLUSTER_CLS = rediscluster.StrictRedisCluster
