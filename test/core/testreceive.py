# docker run -d --rm --name ict_rab -p 5672:5672
# -e "RABBITMQ_ADMIN_PASSWORD=admin" -e "RABBITMQ_OBNL_PASSWORD=obnl" -e "RABBITMQ_TOOL_PASSWORD=tool"
# integrcity/ict-rabbitmq

from obnl.core.client import ClientNode


class ClientTestNode(ClientNode):
    def __init__(
        self,
        host,
        vhost,
        username,
        password,
        config_file,
        data,
        input_attributes=None,
        output_attributes=None,
        is_first=False,
    ):
        super().__init__(host, vhost, username, password, config_file, input_attributes, output_attributes, is_first)
        self._data = data
        self._i = 0

    def step(self, current_time, time_step):
        print("----- " + self.name + " -----")
        print(self.name, time_step)
        print(self.name, current_time)
        print(self.name, self.input_values)

        for o in self.output_attributes:
            rv = self._data[self._i % len(self._data)]
            print(self.name, o, ":", rv)
            self.update_attribute(o, rv)
        print("=============")
        self._i += 1


if __name__ == "__main__":

    data_a = [1, 2, 3, 4]

    data_b = [1.1, 2.2, 3.3, 4.4, 5.5]

    data_c = [0.1, 0.2]

    a = ClientTestNode(
        "localhost",
        "obnl_vhost",
        "obnl",
        "obnl",
        "../data/A.json",
        data_a,
        output_attributes=["t"],
        input_attributes=["seta"],
        is_first=True,
    )

    b = ClientTestNode(
        "localhost",
        "obnl_vhost",
        "obnl",
        "obnl",
        "../data/B.json",
        data_b,
        output_attributes=["t"])

    c = ClientTestNode(
        "localhost",
        "obnl_vhost",
        "obnl",
        "obnl",
        "../data/C.json",
        data_c,
        input_attributes=["t1", "t2"],
        output_attributes=["setc"],
    )

    a.start()
    b.start()
    c.start()
