from odoo.tests import common
import logging
logger = logging.getLogger('product')

_logger = logging.getLogger(__name__)

class TestDemo(common.TransactionCase):
  def test_import_single_product_cost(self):
    test_import = self.env['magento.store'].import_single_product_cost('590010007130102')
    _logger.debug('test start')
    self.assertEqual(test_import, True) ## Fail / Success Depend on data working properly.
    print('Your test was succesfull!')