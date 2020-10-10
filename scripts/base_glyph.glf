# Pointwise V18.3 Journal file - Fri Oct  9 15:30:49 2020

package require PWI_Glyph 3.18.3

pw::Application setUndoMaximumLevels 5
pw::Application reset
pw::Application markUndoLevel {Journal Reset}

pw::Application clearModified

set _TMP(mode_1) [pw::Application begin DatabaseImport]
  $_TMP(mode_1) initialize -strict -type Automatic D:/Github/IdealBifurcations/scripts/generate_steady_foam_cases/step_files/base_01_inlet_1.80_bif_1.0_outlet_1.2_angle_0.STEP
  $_TMP(mode_1) read
  $_TMP(mode_1) convert
$_TMP(mode_1) end
unset _TMP(mode_1)
pw::Application markUndoLevel {Import Database}

pw::Application setGridPreference Unstructured
pw::Connector setCalculateDimensionMethod Spacing
pw::Connector setCalculateDimensionSpacing 0.20000000000000001
set _DB(1) [pw::DatabaseEntity getByName NONE-55]
set _TMP(PW_1) [pw::DomainUnstructured createOnDatabase -parametricConnectors Aligned -merge 0 -reject _TMP(unused) [list $_DB(1)]]
unset _TMP(unused)
unset _TMP(PW_1)
pw::Application markUndoLevel {Domains On DB Entities}

pw::Display setShowDomains 0
set _CN(1) [pw::GridEntity getByName con-18]
set _CN(2) [pw::GridEntity getByName con-30]
set _CN(3) [pw::GridEntity getByName con-33]
set _CN(4) [pw::GridEntity getByName con-37]
set _CN(5) [pw::GridEntity getByName con-21]
set _CN(6) [pw::GridEntity getByName con-4]
set _TMP(PW_1) [pw::DomainUnstructured createFromConnectors -reject _TMP(unusedCons)  [list $_CN(1) $_CN(2) $_CN(3) $_CN(4) $_CN(5) $_CN(6)]]
unset _TMP(unusedCons)
unset _TMP(PW_1)
pw::Application markUndoLevel {Assemble Domains}

set _DM(1) [pw::GridEntity getByName dom-14]
set _DM(2) [pw::GridEntity getByName dom-15]
set _DM(3) [pw::GridEntity getByName dom-13]
set _TMP(mode_1) [pw::Application begin UnstructuredSolver [list $_DM(1) $_DM(2) $_DM(3)]]
  set _TMP(PW_1) [pw::TRexCondition getByName Unspecified]
  set _TMP(PW_2) [pw::TRexCondition create]
  set _TMP(PW_3) [pw::TRexCondition getByName bc-2]
  unset _TMP(PW_2)
  $_TMP(PW_3) setConditionType Wall
  $_TMP(PW_3) setValue 0.025000000000000001
  $_TMP(PW_3) apply [list [list $_DM(3) $_CN(2) Same] [list $_DM(2) $_CN(4) Same] [list $_DM(1) $_CN(6) Same] [list $_DM(1) $_CN(1) Same] [list $_DM(2) $_CN(5) Same] [list $_DM(3) $_CN(3) Same]]
  set _TMP(ENTS) [pw::Collection create]
  $_TMP(ENTS) set [list $_DM(1) $_DM(2) $_DM(3)]
  $_TMP(ENTS) do setUnstructuredSolverAttribute TRexCellType TriangleQuad
  $_TMP(ENTS) do setUnstructuredSolverAttribute TRexMaximumLayers 6
  $_TMP(ENTS) do setUnstructuredSolverAttribute TRexGrowthRate 1.2
  $_TMP(ENTS) do setUnstructuredSolverAttribute TRexGrowthRate 1.1
  $_TMP(ENTS) delete
  unset _TMP(ENTS)
  $_TMP(mode_1) run Initialize
  $_TMP(mode_1) run Refine
$_TMP(mode_1) end
unset _TMP(mode_1)
pw::Application markUndoLevel Solve

set _TMP(mode_1) [pw::Application begin UnstructuredSolver [list $_DM(1) $_DM(2) $_DM(3)]]
$_TMP(mode_1) abort
unset _TMP(mode_1)
unset _TMP(PW_1)
unset _TMP(PW_3)
set _DM(4) [pw::GridEntity getByName dom-1]
set _DM(5) [pw::GridEntity getByName dom-2]
set _DM(6) [pw::GridEntity getByName dom-3]
set _DM(7) [pw::GridEntity getByName dom-9]
set _DM(8) [pw::GridEntity getByName dom-5]
set _DM(9) [pw::GridEntity getByName dom-10]
set _DM(10) [pw::GridEntity getByName dom-12]
set _DM(11) [pw::GridEntity getByName dom-4]
set _DM(12) [pw::GridEntity getByName dom-6]
set _DM(13) [pw::GridEntity getByName dom-8]
set _DM(14) [pw::GridEntity getByName dom-7]
set _DM(15) [pw::GridEntity getByName dom-11]
set _TMP(PW_1) [pw::BlockUnstructured createFromDomains -reject _TMP(unusedDoms) -voids _TMP(voidBlocks) -baffles _TMP(baffleFaces) [concat [list] [list $_DM(1) $_DM(2) $_DM(3) $_DM(4) $_DM(5) $_DM(6) $_DM(7) $_DM(8) $_DM(9) $_DM(10) $_DM(11) $_DM(12) $_DM(13) $_DM(14) $_DM(15)]]]
unset _TMP(unusedDoms)
unset _TMP(PW_1)
pw::Application markUndoLevel {Assemble Blocks}

set _BL(1) [pw::GridEntity getByName blk-1]
set _TMP(mode_1) [pw::Application begin UnstructuredSolver [list $_BL(1)]]
  set _TMP(PW_1) [pw::TRexCondition getByName Unspecified]
  set _TMP(PW_2) [pw::TRexCondition getByName bc-2]
  set _TMP(PW_3) [pw::TRexCondition create]
  set _TMP(PW_4) [pw::TRexCondition getByName bc-3]
  unset _TMP(PW_3)
  set _TMP(PW_5) [pw::TRexCondition create]
  set _TMP(PW_6) [pw::TRexCondition getByName bc-4]
  unset _TMP(PW_5)
  $_TMP(PW_4) setConditionType Wall
  $_TMP(PW_4) setValue 0.20000000000000001
  $_TMP(PW_4) setValue 0.025000000000000001
  $_TMP(PW_6) setConditionType Match
  $_TMP(PW_4) apply [list [list $_BL(1) $_DM(3) Same] [list $_BL(1) $_DM(14) Opposite] [list $_BL(1) $_DM(7) Opposite] [list $_BL(1) $_DM(1) Same] [list $_BL(1) $_DM(6) Opposite] [list $_BL(1) $_DM(13) Opposite] [list $_BL(1) $_DM(8) Opposite] [list $_BL(1) $_DM(9) Opposite] [list $_BL(1) $_DM(10) Opposite] [list $_BL(1) $_DM(4) Opposite] [list $_BL(1) $_DM(12) Opposite] [list $_BL(1) $_DM(5) Opposite] [list $_BL(1) $_DM(11) Opposite] [list $_BL(1) $_DM(2) Same] [list $_BL(1) $_DM(15) Opposite]]
  $_TMP(PW_6) apply [list [list $_BL(1) $_DM(3) Same] [list $_BL(1) $_DM(1) Same] [list $_BL(1) $_DM(2) Same]]
  $_BL(1) setUnstructuredSolverAttribute TRexMaximumLayers 6
  $_BL(1) setUnstructuredSolverAttribute TRexGrowthRate 1.2
  $_BL(1) setUnstructuredSolverAttribute TRexGrowthRate 1.1
  $_TMP(mode_1) setStopWhenFullLayersNotMet true
  $_TMP(mode_1) setAllowIncomplete true
  $_TMP(mode_1) run Initialize
  $_TMP(mode_1) setStopWhenFullLayersNotMet true
  $_TMP(mode_1) setAllowIncomplete true
  $_TMP(mode_1) run Initialize
$_TMP(mode_1) end
unset _TMP(mode_1)
pw::Application markUndoLevel Solve

set _TMP(mode_1) [pw::Application begin UnstructuredSolver [list $_BL(1)]]
$_TMP(mode_1) abort
unset _TMP(mode_1)
unset _TMP(PW_1)
unset _TMP(PW_2)
unset _TMP(PW_4)
unset _TMP(PW_6)
pw::Application setCAESolver OpenFOAM 3
pw::Application markUndoLevel {Select Solver}

set _TMP(PW_1) [pw::BoundaryCondition getByName Unspecified]
set _TMP(PW_2) [pw::BoundaryCondition create]
pw::Application markUndoLevel {Create BC}

set _TMP(PW_3) [pw::BoundaryCondition getByName bc-2]
unset _TMP(PW_2)
set _TMP(PW_4) [pw::BoundaryCondition create]
pw::Application markUndoLevel {Create BC}

set _TMP(PW_5) [pw::BoundaryCondition getByName bc-3]
unset _TMP(PW_4)
set _TMP(PW_6) [pw::BoundaryCondition create]
pw::Application markUndoLevel {Create BC}

set _TMP(PW_7) [pw::BoundaryCondition getByName bc-4]
unset _TMP(PW_6)
set _TMP(PW_8) [pw::BoundaryCondition create]
pw::Application markUndoLevel {Create BC}

set _TMP(PW_9) [pw::BoundaryCondition getByName bc-5]
unset _TMP(PW_8)
$_TMP(PW_3) setPhysicalType -usage CAE wall
pw::Application markUndoLevel {Change BC Type}

$_TMP(PW_5) setPhysicalType -usage CAE patch
pw::Application markUndoLevel {Change BC Type}

$_TMP(PW_7) setPhysicalType -usage CAE patch
pw::Application markUndoLevel {Change BC Type}

$_TMP(PW_9) setPhysicalType -usage CAE patch
pw::Application markUndoLevel {Change BC Type}

$_TMP(PW_3) setName INLET
pw::Application markUndoLevel {Name BC}

$_TMP(PW_3) setName WALL
pw::Application markUndoLevel {Name BC}

$_TMP(PW_5) setName INLET
pw::Application markUndoLevel {Name BC}

$_TMP(PW_7) setName OUTLET_1
pw::Application markUndoLevel {Name BC}

$_TMP(PW_9) setName OUTLET_2
pw::Application markUndoLevel {Name BC}

$_TMP(PW_3) apply [list [list $_BL(1) $_DM(6)] [list $_BL(1) $_DM(1)] [list $_BL(1) $_DM(9)] [list $_BL(1) $_DM(5)] [list $_BL(1) $_DM(7)] [list $_BL(1) $_DM(13)] [list $_BL(1) $_DM(10)] [list $_BL(1) $_DM(8)] [list $_BL(1) $_DM(15)] [list $_BL(1) $_DM(11)] [list $_BL(1) $_DM(12)] [list $_BL(1) $_DM(4)] [list $_BL(1) $_DM(2)] [list $_BL(1) $_DM(3)] [list $_BL(1) $_DM(14)]]
pw::Application markUndoLevel {Set BC}

$_TMP(PW_5) apply [list [list $_BL(1) $_DM(2)]]
pw::Application markUndoLevel {Set BC}

$_TMP(PW_7) apply [list [list $_BL(1) $_DM(3)]]
pw::Application markUndoLevel {Set BC}

$_TMP(PW_9) apply [list [list $_BL(1) $_DM(1)]]
pw::Application markUndoLevel {Set BC}

unset _TMP(PW_1)
unset _TMP(PW_3)
unset _TMP(PW_5)
unset _TMP(PW_7)
unset _TMP(PW_9)
set _TMP(mode_1) [pw::Application begin CaeExport]
  $_TMP(mode_1) addAllEntities
  $_TMP(mode_1) initialize -strict -type CAE D:/Github/IdealBifurcations/scripts/generate_steady_foam_cases/foam_cases/base_01_inlet_1.80_bif_1.0_outlet_1.2_angle_0/constant/polyMesh
  $_TMP(mode_1) verify
  $_TMP(mode_1) write
$_TMP(mode_1) end
unset _TMP(mode_1)
