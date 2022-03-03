#!/usr/bin/env python

import os

job_list = [
"bnxt-roce.xml",
"cxgb4-iw.xml",
"hfi1-opa.xml",
"mlx4-ib.xml",
"mlx4-roce.xml",
"mlx5-ib.xml",
"mlx5-roce.xml",
"qedr-iw.xml"
]

whit_board = ""
distro_name = ""
kernel_repo = "#package_name=kernel"

for job in job_list:
    os.system("git checkout -- %s" % job)
    os.system("sed -i 's,| RDMA sanity <,| RDMA sanity | %s<,g' %s" % (whit_board, job))
    os.system("sed -i 's,<distro_name op=\"=\" value=\"\"/>,<distro_name op=\"=\" value=\"%s\"/>,g' %s" % (distro_name, job))
    os.system("sed -i 's,<param name=\"KPKG_URL\" value=\"\"/>,<param name=\"KPKG_URL\" value=\"%s\"/>,g' %s" % (kernel_repo, job))
    os.system("bkr job-submit %s" % (job))
