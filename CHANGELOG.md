# Changelog

Every noteable change is logged here.

## v0.8.0 (2022-10-18)

### Feature

* add qview cli runner (27c626242489)
* debug root path (2b2fb8e51ef4)

### Chore

* add executable flag (27e7d3ddd728)
* add dev environment (13850960ba13)
* add missing deliver flag (038abdac8755)
* adjust test data generator (b427c5f9c2b3)
* remove default (15c0a5239411)
* remove useless longrun (1e0cae2c71c2)
* remove useless branch and release (b55b97d1fdd4)
* convert nightly to all (5a8e6057abea)
* upgrade baw (9a67d9566a12)
* do not run in privileged mode (5dc72c936dc1)
* upgrade requirements.txt (0e4f236a44ed)
* add missing package (058f77f87214)

## v0.7.0 (2022-10-03)

### Chore

* add separate generator step (be34c2b628e4)
* add Jenkinsfile (c614d01dfef0)
* upgrade requirements.txt (726096c21179)

## v0.6.3

### Documentation

* adjust modules path (fb7ece502df5)
* Happy New Year! (c487cfd6530c)

## v0.6.2

### Fix

* adjust job file name (ff30a787a556)

## v0.6.1

### Fix

* do not fail on empty user selection (d3da04d00c7c)

## v0.6.0

### Feature

* increase width of rendered plot (363f8f19345f)
* set zero as non existing value (a6f324581802)
* add options to collect findings by folder (4a25c8f501b5)

### Fix

* always fill empty data (9eabe067c00b)
* return 404 to avoid client browser caching (eee0c8cf5d45)
* do not break rendering with empty data (e511ebc69f57)
* beautify document name (1caa0def7f20)

## v0.5.1

### Feature

* add grid to increase readability (4d39d7489f9f)

### Fix

* beautify document name (df2ccca31a93)
* overwrite result if already exists (7bde3720998f)
* use default value for non existing data point (77c329568e23)
* limit max finding count to selected findings (c33df0575e16)

## v0.5.0

### Feature

* use selective findings as additional render input (80004e023f63)
* add plot updater (3896df496fc0)
* add parameter to overwrite collected version (4bfe5a475801)
* add method to group data by finding id (194036098611)
* add sync flag to use synchronized renderer (246a4b7c8bdd)
* add conftest basic app (348868a93513)

### Fix

* enable plotting different findings (203bdcc29767)
* do not fail on plain plots call (8b16ad9c9ffb)

### Documentation

* add different plot states (38259b708d53)
* extend interface documentation (20bd712d4d94)

## v0.4.0

### Feature

* add distance to text and div border (681dd839d93e)
* limit plot size height (1c38b078d18e)
* use selected versions (84a76c7d10e7)
* add plot provider (200e6b5b2e63)
* add legend to plot renderer (d98db01a1fbf)
* skip and log pickling error (de13d7967005)
* increase distance between max value and top border (e2b788db2518)
* link renderer to user call, run in parallel (1183383541cc)
* add renderer tmp path (08e32a30d5b8)
* add finding version plot renderer (6f92f9be0f89)
* add method to collect and sort available versions (48dd9a169a52)
* register data API (01a4c582c75e)
* add selected plot provider (79945e7d6a27)
* add multiple filter options (582721912f08)
* render incoming plots (30a48735b07d)
* define plots update API (4320c2630152)
* make findings selectable (3fe6c5bff496)
* collect used finding ids (fa2146cedca0)
* add rpc call (08722d6d461a)
* render list of documents and used versions (89fd5633c0e0)
* add findings and home view (5c1c6c987a31)
* add basic application structure (7be56fbc144e)

## v0.3.0

### Feature

* add list command (1429011e5fd0)

### Fix

* rename collect command to publish (6866ab348664)
* use filename instead of tmp name (297a72f4be3c)

## v0.2.0

### Feature

* connect collect command to data logic (0e69cbaeccf5)
* add config to manage cached global vars (7476d9025425)
* enable dumping single document (22f902547dcd)
* add method to collect cached data from queuemo result (38ca57b9a5b7)

### Fix

* use absolute serialize path (444cfc099128)

## v0.1.0

### Feature

* add method to dump and load single result (8b36670c401d)
* add mechanism to dump and load analyzed projects (a16da8b1acb1)
* add basic document structure (d48a2a3749e2)

### Documentation

* add basic documentation (c8dcd54fcc72)

## v0.0.0 Initial release
