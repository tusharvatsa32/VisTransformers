# weight_dict = {'loss_ce': 1, 'loss_bbox': args.bbox_loss_coef}
weight_dict={'loss_ce':1,'loss_bbox':bbox_loss_coef}
# weight_dict['loss_giou'] = args.giou_loss_coef
weight_dict['loss_giou']=giou_loss_coef
    # if args.masks:
    #     weight_dict["loss_mask"] = args.mask_loss_coef
    #     weight_dict["loss_dice"] = args.dice_loss_coef
if masks:
  weight_dict['loss_mask']=mask_loss_coef
  weight_dict['loss_dice']=dice_loss_coef
    # TODO this is a hack
if aux_loss:
  aux_weight_dict = {}
  for i in range(dec_layers - 1):
    aux_weight_dict.update({k + f'_{i}': v for k, v in weight_dict.items()})
  weight_dict.update(aux_weight_dict)
