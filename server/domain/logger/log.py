#!/usr/bin/env python

import os
import logging
import logging.config
from .settings import LOG_SETTINGS

class Logger:
  def __init__(self, name = __name__, level = None):
      self.name = name
      self.setup_loging(level)

  def setup_loging(self, level = None):
    log_settings = LOG_SETTINGS.copy()

    if level:
        log_settings['root']['level'] = level

    logging.config.dictConfig(LOG_SETTINGS)

    self.create_dirs_if_not_exists()

  def create_dirs_if_not_exists(self):
      if not os.path.exists('logs'):
          os.makedirs('logs')

  def get_logger(self):
     return logging.getLogger(self.name)
