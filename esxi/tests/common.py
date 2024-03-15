# (C) Datadog, Inc. 2024-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from pyVmomi import vim, vmodl

HOST = "127.0.0.1"
PORT = 8989
VCSIM_INSTANCE = {'host': f"{HOST}:{str(PORT)}", 'username': 'test', 'password': 'test'}

BASE_INSTANCE = {'host': 'localhost', 'username': 'test', 'password': 'test'}


PERF_COUNTER_INFO = [
    vim.PerformanceManager.CounterInfo(
        key=1,
        groupInfo=vim.ElementDescription(key='cpu'),
        nameInfo=vim.ElementDescription(key='usage'),
        rollupType=vim.PerformanceManager.CounterInfo.RollupType.average,
        unitInfo=vim.ElementDescription(key='millisecond'),
    ),
    vim.PerformanceManager.CounterInfo(
        key=65541,
        groupInfo=vim.ElementDescription(key='mem'),
        nameInfo=vim.ElementDescription(key='granted'),
        rollupType=vim.PerformanceManager.CounterInfo.RollupType.average,
        unitInfo=vim.ElementDescription(key='kiloBytes'),
    ),
    vim.PerformanceManager.CounterInfo(
        key=4,
        groupInfo=vim.ElementDescription(key='gpu'),
        nameInfo=vim.ElementDescription(key='temperature'),
        rollupType=vim.PerformanceManager.CounterInfo.RollupType.average,
        unitInfo=vim.ElementDescription(key='celcius'),
    ),
    vim.PerformanceManager.CounterInfo(
        key=5678,
        groupInfo=vim.ElementDescription(key='net'),
        nameInfo=vim.ElementDescription(key='droppedRx'),
        rollupType=vim.PerformanceManager.CounterInfo.RollupType.summation,
    ),
]

PERF_METRIC_ID = [
    vim.PerformanceManager.MetricId(counterId=1),
    vim.PerformanceManager.MetricId(counterId=65541),
    vim.PerformanceManager.MetricId(counterId=5678),
]

PERF_ENTITY_METRICS = [
    vim.PerformanceManager.EntityMetric(
        entity=vim.HostSystem(moId="host"),
        value=[
            vim.PerformanceManager.IntSeries(
                value=[23, 26],
                id=vim.PerformanceManager.MetricId(counterId=1),
            )
        ],
    ),
    vim.PerformanceManager.EntityMetric(
        entity=vim.HostSystem(moId="host"),
        value=[
            vim.PerformanceManager.IntSeries(
                value=[10, 80],
                id=vim.PerformanceManager.MetricId(counterId=65541),
            )
        ],
    ),
    vim.PerformanceManager.EntityMetric(
        entity=vim.HostSystem(moId="host"),
        value=[
            vim.PerformanceManager.IntSeries(
                value=[-1],
                id=vim.PerformanceManager.MetricId(counterId=5678),
            )
        ],
    ),
    vim.PerformanceManager.EntityMetric(
        entity=vim.HostSystem(moId="host"),
        value=[
            vim.PerformanceManager.IntSeries(
                value=[],
                id=vim.PerformanceManager.MetricId(counterId=5678),
            )
        ],
    ),
    vim.PerformanceManager.EntityMetric(
        entity=vim.VirtualMachine(moId="vm1"),
        value=[
            vim.PerformanceManager.IntSeries(
                value=[11, 18],
                id=vim.PerformanceManager.MetricId(counterId=1),
            )
        ],
    ),
    vim.PerformanceManager.EntityMetric(
        entity=vim.VirtualMachine(moId="vm2"),
        value=[
            vim.PerformanceManager.IntSeries(
                value=[11, 19],
                id=vim.PerformanceManager.MetricId(counterId=1),
            )
        ],
    ),
    vim.PerformanceManager.EntityMetric(
        entity=vim.VirtualMachine(moId="vm1"),
        value=[
            vim.PerformanceManager.IntSeries(
                value=[12, 28],
                id=vim.PerformanceManager.MetricId(counterId=5678),
            )
        ],
    ),
]

PROPERTIES_EX = vim.PropertyCollector.RetrieveResult(
    objects=[
        vim.ObjectContent(
            obj=vim.HostSystem(moId="host"),
            propSet=[
                vmodl.DynamicProperty(
                    name='name',
                    val='localhost.localdomain',
                ),
                vmodl.DynamicProperty(
                    name='parent',
                    val=vim.Datacenter(moId="dc2"),
                ),
            ],
        ),
        vim.ObjectContent(
            obj=vim.VirtualMachine(moId="vm1"),
            propSet=[
                vmodl.DynamicProperty(
                    name='name',
                    val='vm1',
                ),
                vmodl.DynamicProperty(
                    name='runtime.powerState',
                    val=vim.VirtualMachinePowerState.poweredOn,
                ),
                vmodl.DynamicProperty(
                    name='runtime.host',
                    val=vim.HostSystem(moId="host"),
                ),
                vmodl.DynamicProperty(
                    name='parent',
                    val=vim.Datacenter(moId="dc2"),
                ),
            ],
        ),
        vim.ObjectContent(
            obj=vim.VirtualMachine(moId="vm2"),
            propSet=[
                vmodl.DynamicProperty(
                    name='name',
                    val='vm2',
                ),
                vmodl.DynamicProperty(
                    name='parent',
                    val=vim.ClusterComputeResource(moId="c1"),
                ),
                vmodl.DynamicProperty(
                    name='runtime.powerState',
                    val=vim.VirtualMachinePowerState.poweredOn,
                ),
            ],
        ),
        vim.ObjectContent(
            obj=vim.ClusterComputeResource(moId="c1"),
            propSet=[
                vmodl.DynamicProperty(
                    name='name',
                    val='c1',
                ),
            ],
        ),
        vim.ObjectContent(
            obj=vim.Folder(moId="folder_1"),
            propSet=[
                vmodl.DynamicProperty(
                    name='name',
                    val='folder_1',
                ),
            ],
        ),
        vim.ObjectContent(
            obj=vim.Datacenter(moId="dc2"),
            propSet=[
                vmodl.DynamicProperty(
                    name='name',
                    val='dc2',
                ),
                vmodl.DynamicProperty(
                    name='parent',
                    val=vim.Folder(moId="folder_1"),
                ),
            ],
        ),
    ]
)


VCSIM_HOST_METRICS = [
    'cpu.coreUtilization.avg',
    'cpu.costop.sum',
    'cpu.demand.avg',
    'cpu.idle.sum',
    'cpu.latency.avg',
    'cpu.readiness.avg',
    'cpu.ready.sum',
    'cpu.reservedCapacity.avg',
    'cpu.swapwait.sum',
    'cpu.totalCapacity.avg',
    'cpu.usage.avg',
    'cpu.usagemhz.avg',
    'cpu.used.sum',
    'cpu.utilization.avg',
    'cpu.wait.sum',
    'datastore.datastoreIops.avg',
    'datastore.datastoreMaxQueueDepth.latest',
    'datastore.datastoreNormalReadLatency.latest',
    'datastore.datastoreNormalWriteLatency.latest',
    'datastore.datastoreReadBytes.latest',
    'datastore.datastoreReadIops.latest',
    'datastore.datastoreReadLoadMetric.latest',
    'datastore.datastoreReadOIO.latest',
    'datastore.datastoreVMObservedLatency.latest',
    'datastore.datastoreWriteBytes.latest',
    'datastore.datastoreWriteIops.latest',
    'datastore.datastoreWriteLoadMetric.latest',
    'datastore.datastoreWriteOIO.latest',
    'datastore.maxTotalLatency.latest',
    'datastore.numberReadAveraged.avg',
    'datastore.numberWriteAveraged.avg',
    'datastore.read.avg',
    'datastore.siocActiveTimePercentage.avg',
    'datastore.sizeNormalizedDatastoreLatency.avg',
    'datastore.totalWriteLatency.avg',
    'datastore.write.avg',
    'disk.busResets.sum',
    'disk.commands.sum',
    'disk.commandsAborted.sum',
    'disk.commandsAveraged.avg',
    'disk.deviceLatency.avg',
    'disk.deviceReadLatency.avg',
    'disk.deviceWriteLatency.avg',
    'disk.kernelLatency.avg',
    'disk.kernelReadLatency.avg',
    'disk.kernelWriteLatency.avg',
    'disk.maxQueueDepth.avg',
    'disk.maxTotalLatency.latest',
    'disk.numberRead.sum',
    'disk.numberReadAveraged.avg',
    'disk.numberWrite.sum',
    'disk.numberWriteAveraged.avg',
    'disk.queueLatency.avg',
    'disk.queueReadLatency.avg',
    'disk.queueWriteLatency.avg',
    'disk.read.avg',
    'disk.totalLatency.avg',
    'disk.totalReadLatency.avg',
    'disk.totalWriteLatency.avg',
    'disk.usage.avg',
    'disk.write.avg',
    'hbr.hbrNetRx.avg',
    'hbr.hbrNetTx.avg',
    'hbr.hbrNumVms.avg',
    'mem.active.avg',
    'mem.activewrite.avg',
    'mem.compressed.avg',
    'mem.compressionRate.avg',
    'mem.consumed.avg',
    'mem.decompressionRate.avg',
    'mem.granted.avg',
    'mem.heap.avg',
    'mem.heapfree.avg',
    'mem.latency.avg',
    'mem.llSwapIn.avg',
    'mem.llSwapInRate.avg',
    'mem.llSwapOut.avg',
    'mem.llSwapOutRate.avg',
    'mem.llSwapUsed.avg',
    'mem.lowfreethreshold.avg',
    'mem.overhead.avg',
    'mem.reservedCapacity.avg',
    'mem.shared.avg',
    'mem.sharedcommon.avg',
    'mem.state.latest',
    'mem.swapin.avg',
    'mem.swapinRate.avg',
    'mem.swapout.avg',
    'mem.swapoutRate.avg',
    'mem.swapused.avg',
    'mem.sysUsage.avg',
    'mem.totalCapacity.avg',
    'mem.unreserved.avg',
    'mem.usage.avg',
    'mem.vmfs.pbc.capMissRatio.latest',
    'mem.vmfs.pbc.overhead.latest',
    'mem.vmfs.pbc.size.latest',
    'mem.vmfs.pbc.sizeMax.latest',
    'mem.vmfs.pbc.workingSet.latest',
    'mem.vmfs.pbc.workingSetMax.latest',
    'mem.vmmemctl.avg',
    'mem.zero.avg',
    'net.broadcastRx.sum',
    'net.broadcastTx.sum',
    'net.bytesRx.avg',
    'net.bytesTx.avg',
    'net.droppedRx.sum',
    'net.droppedTx.sum',
    'net.errorsRx.sum',
    'net.errorsTx.sum',
    'net.multicastRx.sum',
    'net.multicastTx.sum',
    'net.packetsRx.sum',
    'net.packetsTx.sum',
    'net.received.avg',
    'net.transmitted.avg',
    'net.unknownProtos.sum',
    'net.usage.avg',
    'power.energy.sum',
    'power.power.avg',
    'power.powerCap.avg',
    'rescpu.actav1.latest',
    'rescpu.actav15.latest',
    'rescpu.actav5.latest',
    'rescpu.actpk1.latest',
    'rescpu.actpk15.latest',
    'rescpu.actpk5.latest',
    'rescpu.maxLimited1.latest',
    'rescpu.maxLimited15.latest',
    'rescpu.maxLimited5.latest',
    'rescpu.runav1.latest',
    'rescpu.runav15.latest',
    'rescpu.runav5.latest',
    'rescpu.runpk1.latest',
    'rescpu.runpk15.latest',
    'rescpu.runpk5.latest',
    'rescpu.sampleCount.latest',
    'rescpu.samplePeriod.latest',
    'storageAdapter.commandsAveraged.avg',
    'storageAdapter.maxTotalLatency.latest',
    'storageAdapter.numberReadAveraged.avg',
    'storageAdapter.numberWriteAveraged.avg',
    'storageAdapter.read.avg',
    'storageAdapter.totalReadLatency.avg',
    'storageAdapter.totalWriteLatency.avg',
    'storageAdapter.write.avg',
    'storagePath.commandsAveraged.avg',
    'storagePath.maxTotalLatency.latest',
    'storagePath.numberReadAveraged.avg',
    'storagePath.numberWriteAveraged.avg',
    'storagePath.read.avg',
    'storagePath.totalReadLatency.avg',
    'storagePath.totalWriteLatency.avg',
    'storagePath.write.avg',
    'sys.resourceCpuAct1.latest',
    'sys.resourceCpuAct5.latest',
    'sys.resourceCpuAllocMax.latest',
    'sys.resourceCpuAllocMin.latest',
    'sys.resourceCpuAllocShares.latest',
    'sys.resourceCpuMaxLimited1.latest',
    'sys.resourceCpuMaxLimited5.latest',
    'sys.resourceCpuRun1.latest',
    'sys.resourceCpuRun5.latest',
    'sys.resourceCpuUsage.avg',
    'sys.resourceFdUsage.latest',
    'sys.resourceMemAllocMax.latest',
    'sys.resourceMemAllocMin.latest',
    'sys.resourceMemAllocShares.latest',
    'sys.resourceMemConsumed.latest',
    'sys.resourceMemCow.latest',
    'sys.resourceMemMapped.latest',
    'sys.resourceMemOverhead.latest',
    'sys.resourceMemShared.latest',
    'sys.resourceMemSwapped.latest',
    'sys.resourceMemTouched.latest',
    'sys.resourceMemZero.latest',
    'sys.uptime.latest',
]

ALL_VCSIM_HOST_METRICS_WITH_VALS = [
    'cpu.totalCapacity.avg',
    'cpu.usage.avg',
    'cpu.ready.sum',
    'cpu.coreUtilization.avg',
    'cpu.idle.sum',
    'cpu.usagemhz.avg',
    'cpu.readiness.avg',
    'cpu.demand.avg',
    'cpu.latency.avg',
    'cpu.utilization.avg',
    'cpu.wait.sum',
    'cpu.used.sum',
    'disk.usage.avg',
    'disk.write.avg',
    'disk.read.avg',
    'mem.heap.avg',
    'mem.consumed.avg',
    'mem.granted.avg',
    'mem.sharedcommon.avg',
    'mem.vmfs.pbc.sizeMax.latest',
    'mem.unreserved.avg',
    'mem.reservedCapacity.avg',
    'mem.active.avg',
    'mem.usage.avg',
    'mem.vmfs.pbc.overhead.latest',
    'mem.vmfs.pbc.workingSetMax.latest',
    'mem.sysUsage.avg',
    'mem.heapfree.avg',
    'mem.vmfs.pbc.workingSet.latest',
    'mem.lowfreethreshold.avg',
    'mem.activewrite.avg',
    'mem.totalCapacity.avg',
    'net.packetsRx.sum',
    'net.broadcastTx.sum',
    'net.bytesRx.avg',
    'net.usage.avg',
    'net.multicastRx.sum',
    'net.multicastTx.sum',
    'net.received.avg',
    'net.transmitted.avg',
    'net.broadcastRx.sum',
    'net.packetsTx.sum',
    'net.bytesTx.avg',
    'rescpu.actpk1.latest',
    'rescpu.runpk1.latest',
    'rescpu.samplePeriod.latest',
    'rescpu.runav5.latest',
    'rescpu.actav1.latest',
    'rescpu.runpk15.latest',
    'rescpu.actav5.latest',
    'rescpu.runav15.latest',
    'rescpu.actpk15.latest',
    'rescpu.actpk5.latest',
    'rescpu.runpk5.latest',
    'rescpu.runav1.latest',
    'rescpu.sampleCount.latest',
    'rescpu.actav15.latest',
    'sys.uptime.latest',
]

FLAKEY_HOST_METRICS = [
    "cpu.costop.sum",
    "datastore.maxTotalLatency.latest",
    "disk.maxTotalLatency.latest",
    "net.multicastTx.sum",
    "storageAdapter.maxTotalLatency.latest",
    "storagePath.maxTotalLatency.latest",
    "sys.resourceCpuAllocMax.latest",
]

VCSIM_VM_METRICS = [
    'cpu.usage.avg',
    'cpu.usagemhz.avg',
    'cpu.wait.sum',
    'cpu.ready.sum',
    'cpu.used.sum',
    'cpu.idle.sum',
    'cpu.swapwait.sum',
    'cpu.latency.avg',
    'cpu.demand.avg',
    'cpu.costop.sum',
    'cpu.readiness.avg',
    'cpu.demandEntitlementRatio.latest',
    'cpu.entitlement.latest',
    'cpu.overlap.sum',
    'cpu.run.sum',
    'mem.usage.avg',
    'mem.granted.avg',
    'mem.active.avg',
    'mem.shared.avg',
    'mem.zero.avg',
    'mem.vmmemctl.avg',
    'mem.overhead.avg',
    'mem.swapin.avg',
    'mem.swapout.avg',
    'mem.consumed.avg',
    'mem.swapinRate.avg',
    'mem.swapoutRate.avg',
    'mem.activewrite.avg',
    'mem.compressed.avg',
    'mem.compressionRate.avg',
    'mem.decompressionRate.avg',
    'mem.latency.avg',
    'mem.llSwapInRate.avg',
    'mem.llSwapOutRate.avg',
    'mem.llSwapUsed.avg',
    'mem.entitlement.avg',
    'mem.overheadMax.avg',
    'mem.overheadTouched.avg',
    'disk.maxTotalLatency.latest',
    'net.usage.avg',
    'net.packetsRx.sum',
    'net.packetsTx.sum',
    'net.received.avg',
    'net.transmitted.avg',
    'net.droppedRx.sum',
    'net.droppedTx.sum',
    'net.bytesRx.avg',
    'net.bytesTx.avg',
    'net.broadcastRx.sum',
    'net.broadcastTx.sum',
    'net.multicastRx.sum',
    'net.multicastTx.sum',
    'net.pnicBytesRx.avg',
    'net.pnicBytesTx.avg',
    'sys.uptime.latest',
    'sys.heartbeat.latest',
    'sys.osUptime.latest',
    'rescpu.actav1.latest',
    'rescpu.actpk1.latest',
    'rescpu.runav1.latest',
    'rescpu.actav5.latest',
    'rescpu.actpk5.latest',
    'rescpu.runav5.latest',
    'rescpu.actav15.latest',
    'rescpu.actpk15.latest',
    'rescpu.runav15.latest',
    'rescpu.runpk1.latest',
    'rescpu.maxLimited1.latest',
    'rescpu.runpk5.latest',
    'rescpu.maxLimited5.latest',
    'rescpu.runpk15.latest',
    'rescpu.maxLimited15.latest',
    'rescpu.sampleCount.latest',
    'rescpu.samplePeriod.latest',
    'datastore.numberReadAveraged.avg',
    'datastore.numberWriteAveraged.avg',
    'datastore.read.avg',
    'datastore.write.avg',
    'datastore.totalReadLatency.avg',
    'datastore.totalWriteLatency.avg',
    'datastore.maxTotalLatency.latest',
    'power.power.avg',
    'power.energy.sum',
    'virtualDisk.write.avg',
    'virtualDisk.read.avg',
]

ALL_VCSIM_VM_METRICS_WITH_VALS = [
    'cpu.ready.sum',
    'cpu.usage.avg',
    'cpu.used.sum',
    'cpu.latency.avg',
    'cpu.idle.sum',
    'cpu.wait.sum',
    'cpu.usagemhz.avg',
    'cpu.readiness.avg',
    'cpu.demand.avg',
    'cpu.run.sum',
    'cpu.overlap.sum',
    'cpu.entitlement.latest',
    'cpu.demandEntitlementRatio.latest',
    'mem.overhead.avg',
    'mem.active.avg',
    'mem.granted.avg',
    'mem.activewrite.avg',
    'mem.consumed.avg',
    'mem.usage.avg',
    'mem.overheadTouched.avg',
    'mem.overheadMax.avg',
    'mem.entitlement.avg',
    'net.multicastRx.sum',
    'net.packetsRx.sum',
    'net.packetsTx.sum',
    'net.bytesTx.avg',
    'net.bytesRx.avg',
    'net.transmitted.avg',
    'net.received.avg',
    'net.usage.avg',
    'net.pnicBytesRx.avg',
    'net.pnicBytesTx.avg',
    'net.broadcastRx.sum',
    'rescpu.actpk5.latest',
    'rescpu.actpk15.latest',
    'rescpu.runpk15.latest',
    'rescpu.actav1.latest',
    'rescpu.runav5.latest',
    'rescpu.actav15.latest',
    'rescpu.runav15.latest',
    'rescpu.sampleCount.latest',
    'rescpu.runpk1.latest',
    'rescpu.actpk1.latest',
    'rescpu.samplePeriod.latest',
    'rescpu.actav5.latest',
    'rescpu.runpk5.latest',
    'rescpu.runav1.latest',
    'sys.uptime.latest',
    'sys.osUptime.latest',
    'sys.heartbeat.latest',
    'virtualDisk.write.avg',
    'virtualDisk.read.avg',
]

FLAKEY_VM_METRICS = [
    'cpu.costop.sum',
    'disk.maxTotalLatency.latest',
    'virtualDisk.read.avg',
]
