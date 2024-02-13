# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['simple_server.py'],
             pathex=['simple_server.py'],
             binaries=[],
             datas=[
			 ('index.html','.'),
			 ('OrbitControls.js','.'),
			 ('stats.module.js','.'),
			 ('STLLoader.js','.'),
			 ('stlviewer.js','.'),
			 ('three.module.min.js','.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          [],
          name='FastSTLViewer',
          debug=False,
          bootloader_ignore_signals=False,
          bootloader_additional_commands=[],
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
