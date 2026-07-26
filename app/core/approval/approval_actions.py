from .approval import create_approval

from .approval_action import ApprovalAction


class ApprovalActions:

    @staticmethod
    def request_delete_project(project):

        return create_approval(

             
            action=ApprovalAction.DELETE_PROJECT,

            title="Delete Project",

            message=(
                f"Are you sure you want to delete "
                f"project '{project.name}'?"
            ),

            payload=project.model_dump(),

        )

    @staticmethod
    def confirm_delete_user(user):

        return create_approval(

            action=ApprovalAction.DELETE_USER,

            title="Delete User",

            message=(
                f"Are you sure you want to delete "
                f"user '{user.name}'?"
            ),

            payload=user.model_dump(),

        )


    # /Later
    # ApprovalActions.confirm_delete_user()

    # ApprovalActions.confirm_delete_company()

    # ApprovalActions.confirm_archive_project()

    # ApprovalActions.confirm_send_email()