# Copyright 2015, Google Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#     * Neither the name of Google Inc. nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""The Python implementation of the GRPC helloworld.Greeter server."""

import time

import addressBook_pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Greeter(addressBook_pb2.EarlyAdopterAddressBookServiceServicer):

  persons= []
 #  def SayHello(self, request, context):
  #   return helloworld_pb2.HelloReply(message='Hello, %s!' % request.name)
  def AddPerson(self,request,context):
      person = request
      self.persons.append(person)
      return addressBook_pb2.AddPersonResponse(msg='Added')
  def GetPerson(self,request,context):
     for person in self.persons:
         if(person.name == request.name):
            return addressBook_pb2.GetPersonResponse(requestedPerson=person)

     return addressBook_pb2.GetPersonResponse(requestedPerson= addressBook_pb2.Person(name='does not exit', id=-1))
  def GetAll(self, request, context):
      return addressBook_pb2.GetAllResponse(person=self.persons)

def serve():
 #  server = helloworld_pb2.early_adopter_create_Greeter_server(
   #    Greeter(), 50051, None, None)
 #  server.start()
  server = addressBook_pb2.early_adopter_create_AddressBookService_server(Greeter(),50051,None,None)
  server.start()
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop()

if __name__ == '__main__':
  serve()
