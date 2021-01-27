import logger

logger.log('This is a log')
logger.info('This is an info')
logger.success('This is a success')
logger.warn('This is a warn')
logger.error('This is an error')

logger.success(f'This is a success with emoji {logger.emoji.party}')