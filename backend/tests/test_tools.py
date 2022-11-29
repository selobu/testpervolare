import pytest
from app import tools
from json import dumps


def test_tools_force_check():
    pass


def test_tools_digest():
    assert (
        tools.digest("1232312312321344523")
        == "fcfc29e5897720bd34e9ceb43e4938c3982405afec65cb8ca56d510587b7ba92"
    )


def test_tools_uuid_isvalid():
    assert tools.uuid_isvalid("16fd2706-8baf-433b-82eb-8c7fada847da")


@pytest.mark.anyio
async def test_tools_paginate_parameters():
    q = "hellostr"
    skip = 2
    limit = 5
    r1 = await tools.paginate_parameters(q, skip, limit)
    assert dumps(r1) == dumps({"q": q, "skip": skip, "limit": limit})


def test_tools_map_name_to_table():
    pass


def test_tools_generate_random():
    for i in range(2, 20):
        assert len(tools.generate_random(i)) == i
