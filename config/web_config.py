"""@package config.web_config
@brief Default Configuration File

An optional web_config_local.py file may be created in this directory. It can
contain a config dictionary which will override the configuration options set
below. Do not modify this file to change local configuration options. It can
also contain a apply_extra_config function which has the same signature as
`apply_config` below.

Configurations are not applied until apply_config is called on the Flask app.
"""
####################################################################
#
#       Web Application Default Config
#
#       Author: Alpha <alpha@pokesplash.net>
####################################################################

import os
import importlib

__all__ = ["config", "load_local_config", "apply_config"]

config = {}
"""@var config Configuration dictionary
@brief This contains the configuration that the application should use.
"""
config['UPLOAD_FOLDER'] = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "../temp/uploads"))
config['ALLOWED_EXTENSIONS'] = ('.txt','.csv')

def apply_extra_config(app):
    """This function should be overridden in web_config_local if provided."""
    return

def load_local_config(conf_module="config.web_config_local", raiseError=True):
    """@brief Loads a configuration from a module
    @param conf_module A string containing the module name. This may use
    my.package.location syntax. This must contain a public `config` dictionary.
    @param raiseError If true, this will raise an exception if the initial
    import fails
    """
    try:
        local_config = importlib.import_module(conf_module).config
        for key in local_config:
            config[key] = local_config[key]
    except ImportError as err:
        if raiseError:
            raise err
        return
    try:
        global apply_extra_config
        apply_extra_config = importlib.import_module(
            conf_module).apply_extra_config
    except AttributeError: # .apply_extra_config is purely optional
        pass

def apply_config(app):
    """
    @brief Set app settings
    """
    app.debug = True
    app.secret_key = '{run python config/web_config.py -c}'
    for key in config:
        app.config[key] = config[key]
    apply_extra_config(app)

load_local_config(raiseError=False)
