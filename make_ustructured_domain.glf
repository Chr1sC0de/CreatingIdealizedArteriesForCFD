# Pointwise V18.3 Journal file - Fri Oct  2 15:52:41 2020

package require PWI_Glyph 3.18.3

pw::Application setUndoMaximumLevels 5

pw::Connector setCalculateDimensionMethod Spacing
pw::Connector setCalculateDimensionSpacing 0.5
set _DB(1) [pw::DatabaseEntity getByName NONE-55]
set _TMP(PW_1) [pw::DomainStructured createOnDatabase -parametricConnectors Aligned -merge 0 -reject _TMP(unused) [list $_DB(1)]]
unset _TMP(unused)
unset _TMP(PW_1)
pw::Application markUndoLevel {Domains On DB Entities}

pw::Application setGridPreference Unstructured
set _TMP(PW_1) [pw::DomainUnstructured createOnDatabase -parametricConnectors Aligned -merge 0 -reject _TMP(unused) [list $_DB(1)]]
unset _TMP(unused)
unset _TMP(PW_1)
pw::Application markUndoLevel {Domains On DB Entities}

pw::Application setGridPreference Structured
