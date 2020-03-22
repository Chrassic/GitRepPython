#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
import sys
# Encoding der Standardausgabe und des Dateisystems herausfinden
stdout_encoding = sys.stdout.encoding or sys.getfilesystemencoding()
fs_encoding = sys.getfilesystemencoding()
# Kompletten Kommandozeilenaufruf übernehmen und nach Unicode umwandeln
cmd_original = " ".join(sys.argv)
cmd_unicode = cmd_original.decode(fs_encoding)
# String verändern und wieder an die Kommandozeile übergeben
cmd_unicode += u" (öäü)"
#print cmd_unicode.encode(stdout_encoding)
