Table of Contents
===
 0. Foreword
 1. Synopsis
 2. Latest Version
 3. Installation
 4. Documentation
 5. Bug Reporting
 6. Contributors
 7. Contacts
 8. License
 9. Copyright

Foreword
===

As OBNL uses AMQP/MQTT protocol (with pika), a server SHALL be running. If docker is 
installed the following command starts a RabbitMQ server:  

    docker run -d --hostname my-rabbit -p 5672:5672 --name some-rabbit rabbitmq:alpine

Synopsis
===
The main purpose of OBNL is simulator communication to simply realise a co-simulation.

Latest Version
===
You can find the latest version of OBNL on:
    https://github.com/ppuertocrem/obnl


Installation
===
OBNL is a full python project thus as long as Python is installed on your
system you can install it by moving in the root folder (the folder this README
file should be) and run:

    python setup.py install
    
In some systems you need Administrator right to run this command.

Warning: OBNL requires these packages to be used in full:

 * pika
 * protobuf


Documentation
===
Currently, the documentation is only accessible in source code.


Bug Reporting
===
If you find any bugs, or if you want new features you can put your request on
github at the following address:

    https://github.com/IntegrCiTy/obnl


Contributors
===

The OBNL Team is currently composed of:

 * Pablo Puerto (pablo.puerto@crem.ch)
 * Gillian Basso (gillian.basso@hevs.ch)
 * Jessen Page (jessen.page@hevs.ch)


Contacts
===
For questions, bug reports, patches and new elements / modules, please use the Bug Reporting.


License
===
You should have received a copy of the Apache License Version 2.0 along with
this program.
If not, see <http://www.apache.org/licenses/LICENSE-2.0>.


Copyright
===
Copyright 2017 The OBNL Team

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.