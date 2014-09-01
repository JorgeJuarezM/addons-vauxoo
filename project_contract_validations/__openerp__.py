# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>). All Rights Reserved
#    d$
###############Credits######################################################
#    Coded by: Vauxoo C.A. (Yanina Aular & Miguel Delgado)
#    Planified by: Rafael Silva
#    Audited by: Vauxoo C.A.
##############################################################################
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name" : "Project Contract Validations",
    "version" : "0.1",
    "depends" : [
                 "project",
                 "sale",
                 ],
    "author" : "Vauxoo",
    "description" : """
        This module adds guidelines and validations in the relation 
        between Project and Analytic Account modules.
    """,
    "website" : "http://vauxoo.com",
    "category" : "Generic Modules",
    "demo" : [],
    "data" : [
        "view/project_view.xml",
    ],
    "active": False,
    "images": [],
    "installable": True,
}
