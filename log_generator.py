import glob
import logging
import os
import random
import time

session_error = True
system_error = True


def check_log_files():
    log_files = glob.glob(os.path.join(directory, '*.log'))

    for log_file in log_files:
        with open(log_file, 'r') as file:
            lines = file.readlines()

        if len(lines) > 200:
            lines = lines[100:]

            with open(log_file, 'w') as file:
                file.writelines(lines)


while True:

    directory = './generated'
    log_levels = [logging.ERROR, logging.WARNING, logging.INFO, logging.DEBUG]
    log_level_probabilities = [0.1, 0.2, 0.4, 0.3]
    log_format = '%(asctime)s [%(levelname)s] %(message)s'  # '%(levelname)s | %(message)s' #'%(asctime)s [%(levelname)s] %(message)s'
    date_format = '%Y-%m-%dT%H:%M:%S'

    logging.basicConfig(level=logging.DEBUG, format=log_format, datefmt=date_format)
    log_level = random.choices(log_levels, weights=log_level_probabilities)[0]

    service_name = f"{random.choice(['Auth', 'Database', 'Web', 'App'])} Service"

    formatter = logging.Formatter(fmt=log_format, datefmt=date_format)
    logger = logging.getLogger(f'{service_name}')
    file_handler = logging.FileHandler(f'{directory}/{service_name}.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    if log_level == 10:
        message = f"{service_name}: {random.choice(['verbose mode enabled', 'running in debug mode', 'tests completed'])}"
        logger.log(logging.DEBUG, message)

    elif log_level == 20:
        message = f"{service_name}: {random.choice(['received request', 'cleaning data', 'connection established'])}"
        logger.log(logging.INFO, message)

    elif log_level == 30:
        message = f"{service_name}: {random.choice(['high CPU usage', 'low disk space', 'connection timeout'])}"
        logger.log(logging.WARNING, message)

    elif log_level == 40:

        prob = random.randint(1, 100)

        if prob >= 75 and service_name == 'Auth Service' and session_error == True:
            time.sleep(10.0)
            session_id = random.randint(10000, 99999)
            info1 = f'Auth Service: New Session Request | Method - Username/Password | Session ID = {session_id}'
            logger.log(logging.INFO, info1)
            time.sleep(2.0)
            warn1 = f'Auth Service: Invalid Token | Token Expired! Retry! | Session ID = {session_id}'
            logger.log(logging.WARNING, warn1)
            logger.log(logging.WARNING, warn1)
            logger.log(logging.WARNING, warn1)
            logger.log(logging.WARNING, warn1)
            logger.log(logging.WARNING, warn1)
            time.sleep(2.0)
            error1 = f'Auth Service: Too Many Failing Login Attempts | Rejecting Proceeding Requests | Session ID = {session_id}'
            logger.log(logging.ERROR, error1)
            time.sleep(2.0)
            info2 = f'Auth Service: Session Closed | Cleaning Session Data... | Session ID = {session_id}'
            logger.log(logging.INFO, info2)
            time.sleep(2.0)

        if 75 > prob >= 50 and system_error == True:
            time.sleep(30)
            services = ['Auth Service', 'Database Service', 'Web Service', 'App Service']
            for service_name in services:
                formatter = logging.Formatter(fmt=log_format, datefmt=date_format)
                logger = logging.getLogger(f'{service_name}')
                file_handler = logging.FileHandler(f'{directory}/{service_name}.log')
                file_handler.setFormatter(formatter)
                logger.addHandler(file_handler)

                message = f"{service_name}: INSUFFICIENT RESOURCES | DISK SPACE FULL! | Restarting Service..."
                logger.log(logging.ERROR, message)
            time.sleep(30)

        else:
            message = f"{service_name}: {random.choice(['memory conflict', 'unknown error', 'unhandled request'])}"
            logger.log(log_level, message)

    logger.removeHandler(file_handler)
    file_handler.close()

    check_log_files()

    time.sleep(random.uniform(2, 5))
