# -*- coding: utf-8 -*-
# vi:si:et:sw=4:sts=4:ts=4

##
## Copyright (C) 2012 Async Open Source <http://www.async.com.br>
## All rights reserved
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., or visit: http://www.gnu.org/.
##
## Author(s): Stoq Team <stoq-devel@async.com.br>
##

from decimal import Decimal

from stoqlib.gui.editors.sellableeditor import SellableTaxConstantEditor
from stoqlib.gui.test.uitestutils import GUITest


class TestSellableTaxConstantEditor(GUITest):
    def testCreate(self):
        editor = SellableTaxConstantEditor(self.store)
        self.check_editor(editor, 'editor-sellabletaxconstant-create')

    def test_confirm(self):
        editor = SellableTaxConstantEditor(self.store)
        self.assertNotSensitive(editor.main_dialog, ['ok_button'])

        editor.description.update('random tax')
        editor.tax_value.update(Decimal('20'))

        self.assertSensitive(editor.main_dialog, ['ok_button'])
        self.check_editor(editor, 'editor-sellableeditor-confirm-filled')

        editor.main_dialog.confirm()
        self.check_editor(editor, 'editor-sellableeditor-confirm',
                          [editor.retval])
