;FLAVOR:Marlin
;TIME:1855
;Filament used: 1.28228m
;Layer height: 0.1
;Generated with Cura_SteamEngine 3.3.1
M104 S190
M109 S190
M82 ;absolute extrusion mode
G28 ;Home
G1 Z15.0 F6000 ;Move the platform down 15mm
G92 E0
G1 F200 E1
G92 E0
G92 E0
G1 F1500 E-4
;LAYER_COUNT:199
;LAYER:0
M107
G0 F3600 X17.8 Y-9.883 Z0.3
;TYPE:SKIRT
G1 F1500 E0
;TIME_ELAPSED:114.534172
;LAYER:1
;LIFT HEIGHT
G0 F3600 Z110.0;QUICK LIFT
G0 F5.0 Z120.0;HOLD TIME
M106 S255
G0 F5400 X9 Y9 Z0.4                        z line getting written twice
G0 F5400 X9 Y9 Z0.52
;TYPE:WALL-INNER
G1 F2700 X-9 Y9 E155.05047
G1 X-9 Y-9 E155.34981
G0 F5400 X-8.429 Y-7.975
G1 F1800 X-7.975 Y-8.429 E171.46638
G0 F5400 X9 Y9
;TIME_ELAPSED:148.304308
;LAYER:2
G0 F7200 X9 Y9 Z0.5
G0 F7200 X9 Y9 Z0.62
;TYPE:WALL-INNER
G1 F3600 X-9 Y9 E171.76572
G1 X-9 Y-9 E172.06507
G0 F7200 X-7.409 Y8.429
G1 F1800 X-8.429 Y7.409 E188.17096
G1 X-8.499 Y7.339
G0 F7200 X-8.429 Y7.975
G1 F1800 X-7.975 Y8.429 E188.18163
G0 F7200 X9 Y9
;TIME_ELAPSED:181.349940
;LAYER:3
G0 X9 Y9 Z0.6
G0 X9 Y9 Z0.72
;TYPE:WALL-INNER
G1 F3600 X-9 Y9 E188.48098
G1 X-9 Y-9 E188.78032
G1 X9 Y-9 E189.07966
G1 X9 Y9 E189.379
G0 F7200 X9.4 Y9.4
G1 F3600 X-9.4 Y9.4 E189.69165
G1 X-9.4 Y-9.4 E190.00429
G1 X9.4 Y-9.4 E190.31694
G1 X9.4 Y9.4 E190.62958
G0 F7200 X9.8 Y9.8
;TYPE:WALL-OUTER
G1 F1800 X-9.8 Y9.8 E190.95553
G1 X-9.8 Y-9.8 E191.28148
G1 X9.8 Y-9.8 E191.60743
G1 X9.8 Y9.8 E191.93338
G0 F7200 X9.6 Y9.8
G0 X9.33 Y9.33
G0 X8.61 Y8.61
;TYPE:SKIN
G1 F1800 X-8.61 Y8.61 E192.21975
G1 X-8.61 Y-8.61 E192.50612
G1 X8.61 Y-8.61 E192.79249
G1 X8.61 Y8.61 E193.07886
G0 F7200 X-7.409 Y-8.429
G1 F1800 X-8.429 Y-7.409 E204.88621
G1 X-8.499 Y-7.339
G0 F7200 X-8.429 Y-7.975
G1 F1800 X-7.975 Y-8.429 E204.89689
G0 F7200 X9 Y9
;TIME_ELAPSED:214.311312
;LAYER:4
G0 X9 Y9 Z0.7
G0 X9 Y9 Z0.82
;TYPE:WALL-INNER
G0 F7200 X-7.409 Y-8.429
G1 F1800 X-8.429 Y-7.409 E1282.27171
G1 X-8.499 Y-7.339
G0 F7200 X-8.429 Y-7.975
G1 F1800 X-7.975 Y-8.429 E1282.28239
;TIME_ELAPSED:1855.373739
G1 F1500 E1278.28239
M107
M104 S0
M140 S0
;Retract the filament
G92 E1
G1 E-1 F300
G28 X0 Y0
M84
M82 ;absolute extrusion mode
M104 S0
;End of Gcode
;SETTING_3 {"global_quality": "[general]\\nversion = 3\\nname = Fine #2\\ndefini
;SETTING_3 tion = fdmprinter\\n\\n[metadata]\\ntype = quality_changes\\nsetting_
;SETTING_3 version = 4\\nquality_type = normal\\n\\n[values]\\nsupport_tree_enab
;SETTING_3 le = True\\n\\n", "extruder_quality": ["[general]\\nversion = 3\\nnam
;SETTING_3 e = Fine #2\\ndefinition = fdmprinter\\n\\n[metadata]\\ntype = qualit
;SETTING_3 y_changes\\nposition = 0\\nsetting_version = 4\\nquality_type = norma
;SETTING_3 l\\n\\n[values]\\ngradual_infill_steps = 3\\ninfill_pattern = cubic\\
;SETTING_3 ninfill_sparse_density = 30\\nwall_thickness = 1.2\\n\\n", "[general]
;SETTING_3 \\nversion = 3\\nname = Fine #2\\ndefinition = fdmprinter\\n\\n[metad
;SETTING_3 ata]\\ntype = quality_changes\\nposition = 1\\nsetting_version = 4\\n
;SETTING_3 quality_type = normal\\n\\n[values]\\n\\n", "[general]\\nversion = 3\
;SETTING_3 \nname = Fine #2\\ndefinition = fdmprinter\\n\\n[metadata]\\ntype = q
;SETTING_3 uality_changes\\nposition = 2\\nsetting_version = 4\\nquality_type = 
;SETTING_3 normal\\n\\n[values]\\n\\n", "[general]\\nversion = 3\\nname = Fine #
;SETTING_3 2\\ndefinition = fdmprinter\\n\\n[metadata]\\ntype = quality_changes\
;SETTING_3 \nposition = 3\\nsetting_version = 4\\nquality_type = normal\\n\\n[va
;SETTING_3 lues]\\n\\n", "[general]\\nversion = 3\\nname = Fine #2\\ndefinition 
;SETTING_3 = fdmprinter\\n\\n[metadata]\\ntype = quality_changes\\nposition = 4\
;SETTING_3 \nsetting_version = 4\\nquality_type = normal\\n\\n[values]\\n\\n", "
;SETTING_3 [general]\\nversion = 3\\nname = Fine #2\\ndefinition = fdmprinter\\n
;SETTING_3 \\n[metadata]\\ntype = quality_changes\\nposition = 5\\nsetting_versi
;SETTING_3 on = 4\\nquality_type = normal\\n\\n[values]\\n\\n", "[general]\\nver
;SETTING_3 sion = 3\\nname = Fine #2\\ndefinition = fdmprinter\\n\\n[metadata]\\
;SETTING_3 ntype = quality_changes\\nposition = 6\\nsetting_version = 4\\nqualit
;SETTING_3 y_type = normal\\n\\n[values]\\n\\n", "[general]\\nversion = 3\\nname
;SETTING_3  = Fine #2\\ndefinition = fdmprinter\\n\\n[metadata]\\ntype = quality
;SETTING_3 _changes\\nposition = 7\\nsetting_version = 4\\nquality_type = normal
;SETTING_3 \\n\\n[values]\\n\\n"]}
