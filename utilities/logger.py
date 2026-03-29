"""
Custom logging utility for framework
"""
import logging
import os
from datetime import datetime
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.config import Config

class Logger:
    """Custom logger class for test execution logging"""
    
    @staticmethod
    def get_logger(name=__name__):
        """
        Creates and returns logger instance
        Args:
            name (str): Logger name
        Returns:
            Logger: Configured logger instance
        """
        # Create logs directory if not exists
        os.makedirs(Config.LOGS_DIR, exist_ok=True)
        
        # Create logger
        logger = logging.getLogger(name)
        logger.setLevel(getattr(logging, Config.LOG_LEVEL))
        
        # Avoid duplicate handlers
        if logger.handlers:
            return logger
        
        # File handler
        log_file = os.path.join(
            Config.LOGS_DIR, 
            f"test_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        )
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # Formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        # Add handlers
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        return logger
