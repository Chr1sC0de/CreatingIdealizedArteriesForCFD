# Pointwise V18.3 Journal file - Fri Oct 30 16:03:46 2020

package require PWI_Glyph 3.18.3

pw::Application setUndoMaximumLevels 5
pw::Application reset
pw::Application markUndoLevel {Journal Reset}

pw::Application clearModified

set _TMP(mode_1) [pw::Application begin DatabaseImport]
$_TMP(mode_1) abort
unset _TMP(mode_1)
set _TMP(mode_1) [pw::Application begin DatabaseImport]
  $_TMP(mode_1) initialize -strict -type Automatic D:/Github/IdealBifurcations/scripts/generate_steady_foam_cases/step_files/base_01_inlet_3.60_bif_2.0_outlet_2.4_angle_0.STEP
  $_TMP(mode_1) read
  $_TMP(mode_1) convert
$_TMP(mode_1) end
unset _TMP(mode_1)
pw::Application markUndoLevel {Import Database}

pw::Connector setCalculateDimensionMethod Spacing
pw::Connector setCalculateDimensionSpacing 0.20000000000000001
set _DB(1) [pw::DatabaseEntity getByName NONE-56]
set _TMP(PW_1) [pw::Collection create]
$_TMP(PW_1) set [list $_DB(1)]
$_TMP(PW_1) do setRenderAttribute FillMode None
$_TMP(PW_1) delete
unset _TMP(PW_1)
pw::Application markUndoLevel {Modify Entity Display}

pw::Application setGridPreference Unstructured
set _TMP(PW_1) [pw::DomainUnstructured createOnDatabase -parametricConnectors Aligned -merge 0 -reject _TMP(unused) [list $_DB(1)]]
unset _TMP(unused)
unset _TMP(PW_1)
pw::Application markUndoLevel {Domains On DB Entities}

pw::Display setShowDatabase 0
pw::Display setShowBodyAxes 0
pw::Display setShowXYZAxes 0
pw::Display setShowDatabase 0
pw::Display setShowSources 0
pw::Display setShowNodes 0
pw::Display setShowConnectors 0
pw::Display setShowDomains 0
pw::Display setShowDrawingGuide 0
pw::Display setShowViewManipulator 0
pw::Display setShowOverset 0
pw::Display setShowBodyAxes 1
pw::Display setShowXYZAxes 1
pw::Display setShowDatabase 1
pw::Display setShowSources 1
pw::Display setShowNodes 1
pw::Display setShowConnectors 1
pw::Display setShowDomains 1
pw::Display setShowDrawingGuide 1
pw::Display setShowViewManipulator 1
pw::Display setShowOverset 1
pw::Display setShowBodyAxes 0
pw::Display setShowXYZAxes 0
pw::Display setShowDatabase 0
pw::Display setShowSources 0
pw::Display setShowNodes 0
pw::Display setShowConnectors 0
pw::Display setShowDomains 0
pw::Display setShowDrawingGuide 0
pw::Display setShowViewManipulator 0
pw::Display setShowOverset 0
pw::Display setShowDomains 1
pw::Display setShowDomains 0
pw::Display setShowConnectors 1
set _CN(1) [pw::GridEntity getByName con-7]
set _CN(2) [pw::GridEntity getByName con-1]
set _CN(3) [pw::GridEntity getByName con-28]
set _CN(4) [pw::GridEntity getByName con-37]
set _CN(5) [pw::GridEntity getByName con-31]
set _CN(6) [pw::GridEntity getByName con-35]
set _TMP(PW_1) [pw::DomainUnstructured createFromConnectors -reject _TMP(unusedCons)  [list $_CN(1) $_CN(2) $_CN(3) $_CN(4) $_CN(5) $_CN(6)]]
unset _TMP(unusedCons)
unset _TMP(PW_1)
pw::Application markUndoLevel {Assemble Domains}

pw::Display setShowDomains 1
