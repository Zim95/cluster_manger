from models import (
    user_model, state_model,
    region_model, instance_model,
    cluster_model, machine_model,
    machine_tags_model
)


def migrate_base_models(model_list):
    for model in model_list:
        model.migrate()


def migrate_models(model_list):
    for model in model_list:
        model.migrate()


def drop_table(model_list):
    for model in model_list:
        model.drop_table()


def migrate_all():
    ''' base models '''
    user_model_obj = user_model.UserModel()
    state_model_obj = state_model.StateModel()
    region_model_obj = region_model.RegionModel()
    instance_model_obj = instance_model.InstanceModel()

    ''' foreign key models '''
    cluster_model_obj = cluster_model.ClusterModel()
    machine_model_obj = machine_model.MachineModel()
    machine_tags_model_obj = machine_tags_model.MachineTagsModel()

    migrate_base_models(
        [user_model_obj, state_model_obj,
         region_model_obj, instance_model_obj]
    )

    migrate_models(
        [cluster_model_obj, machine_model_obj,
         machine_tags_model_obj]
    )
